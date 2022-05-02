from typing import Any, Iterable

import math


def doubles(data: Iterable[Any]) -> list[Any]:
    """Doubles whatever is in `data`."""
    return [2 * _ for _ in data]


def halves(data: Iterable[Any]) -> list[Any]:
    """Halves whatever is in `data`."""
    return [_ / 2 for _ in data]


def impedanceOhm(impedanceLogOhm: float):
    return math.pow(10, impedanceLogOhm)


def impedancekOhmCm2(impedanceOhm: float):
    return impedanceOhm * 0.785 / 1000.0


def inhibitorEfficiencyEIS24h(impedancekOhmCm2: float):
    return ( 1.0 - 13.562/impedancekOhmCm2 ) * 100.0


def inhibitorEfficiencyEIS2h(impedanceLogOhm2h: float):
    ohm = math.pow(10, impedanceLogOhm2h)
    impflux  = ohm*0.785/1000.
    eff = (1-14.025/impflux)*100
    return eff


def inhibitorEfficiencyLPR24h(lpr24h: float):
    impflux = lpr24h * 0.785 / 1000.
    return ( 1. - 11.27815/impflux ) * 100.


def inhibitorEfficiencyPDP(lpr24h: float):
    return lpr24h * 0.785 / 1000.


### Local functions representing KB items


def impkflux(ImpedanceOhm: Iterable[float]) -> list[float]:
    return [impedancekOhmCm2(_) for _ in ImpedanceOhm]


def imp_to_eis(ImpedancekOhmCm2: Iterable[float]) -> list[float]:
    return [inhibitorEfficiencyEIS24h(_) for _ in ImpedancekOhmCm2]


def imp_to_lpr(LPR24h: Iterable[float]) -> list[float]:
    return [inhibitorEfficiencyLPR24h(_) for _ in LPR24h]


def cas_to_smiles(CASNumber: Iterable[str]) -> list[str]:
    import cirpy

    return [cirpy.resolve(_, "smiles") for _ in CASNumber]


def cas_to_inchi(CASNumber: Iterable[str]) -> list[str]:
    import cirpy

    return [cirpy.resolve(_, "stdinchi") for _ in CASNumber]


def imp_pow_func(ImpedanceLogOhm: Iterable[float]) -> list[float]:
    return [impedanceOhm(_) for _ in ImpedanceLogOhm]


# def cas_to_cas(CASNumber: Iterable[str]) -> list[str]:
#     return list(CASNumber)
