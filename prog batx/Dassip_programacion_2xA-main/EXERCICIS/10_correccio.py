effective: dict = {
    'aigua' : {
        'effective' : ['foc'],
        'non_effective' : ['aigua', 'planta']
    },
    'foc' : {
        'effective' : ['planta'],
        'non_effective' : ['aigua','foc']
    },
    'planta' : {
        'effective' : ['aigua'],
        'non_effective' : ['foc','planta']
    },
    'electric' : {
        'effective' : ['aigua'],
        'non_effective' : ['planta', 'electric']
    }
    }


def potencia(atacant, defensor, v_atac, v_def):

    def efectivity(tipoA, tipoB):
        if tipoB in effective[tipoA]['effective']:
            return 2
        elif tipoB in effective[tipoA]['non_effectiv']:
            return 0.5
        else:
            return 0 

    if v_atac < 0 or v_def < 0 or v_atac > 100 or v_def > 100 :
        return 'error'
    
    efectivitat = efectivity(atacant, defensor)
    return(v_atac/v_def) * efectivitat


atacant = input().strip()
defensor = input().strip()
v_atac = int(input())
v_def = int(input())

print(potencia(atacant, defensor, v_atac, v_def))