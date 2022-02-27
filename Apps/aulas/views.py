from django.utils import timezone
from django.shortcuts import render, redirect
from Apps.turmas.models import Escola, Turma
from Apps.usuarios.models import Usuario
from Apps.usuarios.views import auth
from Apps.tools.views import decode, gradePlanUpload
from Apps.tools.data_choices import MONTHS
from .models import GradePlanComment, GradePlan
from django.db.models import Count, Q



def GradePlansView(request):

    mode = request.GET.get('mode', None)
    user = auth(request)
    card_titles = {'viewed': 'Vistos', 'unviewed': 'Não vistos', 'comment': 'Comentados'}
    group_filter = {'viewed': False}

    if user.grupo.nome != 'administrador':
        group_filter['posted_by'] = user

    if user.grupo.nome != 'administrador' and mode == 'comment':
        group_filter['class_plan__posted_by'] = group_filter.pop('posted_by')


    data = {
        'turmas': Turma.objects.filter(professor__id=auth(request).id).count() == 0 and auth(request) == 'professor',
        'mode': mode,
        'card_title': card_titles[mode]
    }


    if mode == 'viewed':
        group_filter['viewed'] = True
        data['data'] = GradePlan.objects.filter(**group_filter).order_by('-id')
    if mode == 'unviewed':
        data['data'] = GradePlan.objects.filter(**group_filter).order_by('-id')
    if mode == 'comment':
        data['data'] = GradePlanComment.objects.values('class_plan__id', 'class_plan__posted_by__nome', 'class_plan__lesson_month', 'class_plan__school__nome').filter(**group_filter).annotate(Count('class_plan__id'))

    data = {**data, **getClassPlans(user)}


    return render(request, 'aulas/planejamentos.html', data)




def PlanejamentoRespostaView(request):
    planejamento = int(decode(request.GET['p']))
    posted_by = auth(request)

    if request.method == 'POST':
        resposta = GradePlanComment()
        resposta.class_plan = GradePlan.objects.get(id=planejamento)
        resposta.message = request.POST['mensagem']
        resposta.posted_by = Usuario.objects.get(id=posted_by.id)
        resposta.save()
        return redirect('../gradeplans/?mode=viewed')

    data = {
        'grade_plan': GradePlan.objects.get(id=planejamento),
        'grade_plan_comments': GradePlanComment.objects.filter(class_plan__id=planejamento).order_by('-creation_date'),
    }

    data = {**data, **getClassPlans(posted_by)}

    return render(request, 'aulas/responder.html', data)


def NovoPlanejamentoView(request):
    posted_by = auth(request)
    document = request.FILES.get('document', None)

    if request.method == 'POST':
        grade_plan = GradePlan()
        grade_plan.posted_by = posted_by
        grade_plan.school = Escola.objects.get(id=request.POST['school'])
        grade_plan.lesson_month = f"{timezone.now().year}-{request.POST['month']}-01"
        grade_plan.description = request.POST['description']
        if document != None:
            url = f"ClassPlan/{grade_plan.lesson_month}/{grade_plan.school.id}_{grade_plan.school.nome}/"
            grade_plan.document = gradePlanUpload(document, url + f"/{posted_by.id}_{grade_plan.school.nome}_{request.POST['month']}")
        grade_plan.save()
        return redirect('../gradeplans/?mode=viewed')

    data = {
        'escolas': Turma.objects.values('escola__nome', 'escola__id').filter(professor__id=auth(request).id).distinct(),
        'months': MONTHS
    }

    data = {**data, **getClassPlans(posted_by)}

    return render(request, 'aulas/newplan.html', data)




def VisualizarView(request):
    
    plan_id = int(decode(request.GET['p']))
    user = auth(request)
    grade_plan = GradePlan.objects.get(id=plan_id)
    grade_plan_comments = GradePlanComment.objects.filter(class_plan__id=plan_id).order_by('-id')

    if grade_plan.posted_by != user:
        grade_plan.viewed = True
        grade_plan.save()
    
    grade_plan_comments.filter(~Q(posted_by=user), viewed=False).update(viewed=True)

    data = {
        'grade_plan': grade_plan,
        'plan_comments': grade_plan_comments
    }

    data = {**data, **getClassPlans(user)}

    return render(request, 'aulas/visualizar.html', data)




def EnviadosView(request):
    user = auth(request)
    data = {
        'turmas': Turma.objects.filter(professor__id=user.id).count() == 0 and user.grupo.nome == 'professor'
    }
    data = {**data, **getClassPlans(user)}

    return render(request, 'aulas/enviados.html', data)




def getClassPlans(user):

    viewed_filter = { 'viewed': True }
    unviewed_filter = { 'viewed': False }

    data = {
        'unviewed_comments': GradePlanComment.objects.filter(~Q(posted_by=user), viewed=False).order_by('-id'),
    }

    if user.grupo.nome != 'administrador':
        viewed_filter['posted_by'] = unviewed_filter['posted_by'] = user
        data['unviewed_comments'] = data['unviewed_comments'].filter(class_plan__posted_by=user)

    data['grade_plans'] = GradePlan.objects.filter(**viewed_filter).order_by('-id')
    data['unviewed_plans'] = GradePlan.objects.filter(**unviewed_filter)

    return data