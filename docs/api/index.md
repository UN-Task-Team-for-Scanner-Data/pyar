# API Overview

Fundamentally, `pyar` consists of (1) a "toolbox" of price index method implementations that can be used by practitioners and (2) a data model for working with price indexes, product classifications, and price index aggregation structures.

## Price Index Toolbox

```mermaid
classDiagram

    direction TB

    class pyar.multilaterals {
        <<module: multilaterals.py>>
        +geks(price: npt.ArrayLike, quantity: npt.ArrayLike, time: npt.ArrayLike, product: npt.ArrayLike, window: int, formula: Callable[<<formulas.py>>]) PriceIndex
    }

    class pyar.formulas {
        <<module: formulas.py>>
        +carli_index(p1: npt.ArrayLike, p2: npt.ArrayLike, na_rm: bool = False) float
        +dutot_index(p1: npt.ArrayLike, p2: npt.ArrayLike, na_rm: bool = False) float
        +jevons_index(p1: npt.ArrayLike, p2: npt.ArrayLike, na_rm: bool = False) float
        +coggeshall_index(p1: npt.ArrayLike, p2: npt.ArrayLike, na_rm: bool = False) float
        "...()"
    }


    class pyar.means {
    <<module: means.py>>
        +generalized_mean(x: npt.ArrayLike, weights: npt.ArrayLike, order: float = 1, na_rm: bool = False) npt.ArrayLike

        +extended_mean(x: npt.ArrayLike, y: npt.ArrayLike, order: float = 1, tol: float = epsilon**0.5, na_rm: bool = False) npt.ArrayLike

        +lehmer_mean( x: npt.ArrayLike, weights: npt.ArrayLike, order: float = 2, na_rm: bool = False) npt.ArrayLike

        +nested_generalized_mean(x: npt.ArrayLike, weights: npt.ArrayLike, order: Tuple[float] = (0, (1, -1)), na_rm: bool = False) npt.ArrayLike
    }

    pyar.formulas ..> pyar.means: uses
    pyar.multilaterals ..> pyar.formulas: uses
```

## Object Model

```mermaid
classDiagram
    direction TB

    class PriceIndex {
        -_index: xr.DataArray
        +__init__(elementals: xr.DataArray): PriceIndex
        +merge(List[PriceIndex]): PriceIndex
        +chain(): PriceIndex
        +aggregate(pias: AggregationStructure): PriceIndex
    }

    class AggregationStructure {
        -_pias: xr.DataArray
        +levels: List[str]
        +expand(): AggregationStructure
    }

    PriceIndex ..> AggregationStructure: uses
```