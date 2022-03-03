from Apps.tools.privacy_data import SEGMENTOS

GRADE_SHIFTS = (
    ('M', 'Manhã'),
    ('CM', 'Contraturno manhã'),
    ('T', 'Tarde'),
    ('CT', 'Contraturno tarde'),
    ('N', 'Noite'),
    ('CN', 'Contraturno noite')
)

GRADE_SEGMENTS = (
    ('infantil', 'Infantil'),
    ('anos_iniciais', 'Anos iniciais'),
    ('anos_finais', 'Anos finais'),
    ('medio', 'Médio')
)

GRADE_PLAN_EMPHASIS = (
    ('T', 'Técnico'),
    ('P', 'Propedêutico'),
)

MONTHS = (
    ('1', 'Janeiro'),
    ('2', 'Fevereiro'),
    ('3', 'Março'),
    ('4', 'Abril'),
    ('5', 'Maio'),
    ('6', 'Junho'),
    ('7', 'Julho'),
    ('8', 'Agosto'),
    ('9', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro'),
)

WEAK_DAYS = (
    ('1', 'Segunda'),
    ('2', 'Terça'),
    ('3', 'Quarta'),
    ('4', 'Quinta'),
    ('5', 'Sexta'),
    ('6', 'Sábado'),
)

COURSEWARE = {
    'GRADE_BOOK': ['Alfa', 'Beta', 'Gama', '1º ano', '2º ano', '3º ano', '4º ano', '5º ano', '6º ano', '7º ano', '8º ano', '9º ano', 'Psi', 'Delta'],
    'EDITION': ['2018', '2019', '2020', '2021', '2022'],
    'VOLUME': ['1', '2', 'Papert', 'Galileu']
}

def gradesPerSegments(segment):
    return SEGMENTOS[segment]