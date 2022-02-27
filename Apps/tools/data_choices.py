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

def gradesPerSegments(segment):
    return SEGMENTOS[segment]