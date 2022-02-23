from Apps.tools.privacy_data import SEGMENTOS

CLASS_SHIFTS = (
    ('M', 'Manhã'),
    ('CM', 'Contraturno manhã'),
    ('T', 'Tarde'),
    ('CT', 'Contraturno tarde'),
    ('N', 'Noite'),
    ('CN', 'Contraturno noite')
)

CLASS_SEGMENTS = (
    ('infantil', 'Infantil'),
    ('anos_iniciais', 'Anos iniciais'),
    ('anos_finais', 'Anos finais'),
    ('medio', 'Médio')
)

CLASS_PLAIN_EMPHASIS = (
    ('T', 'Técnico'),
    ('P', 'Propedêutico'),
)

def classesPerSegments(segment):
    return SEGMENTOS[segment]