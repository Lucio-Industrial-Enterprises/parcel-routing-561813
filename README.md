# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a shipping quote
in dollars.

| Parameter | Values | Notes |
|-----------|--------|-------|
| `weight_kg` | positive float | Parcel weight in kilograms |
| `zone` | `"local"`, `"regional"` | Delivery zone |
| `service` | `"standard"` *(default)*, `"express"` | Express adds a flat $7 surcharge |

Raises `ValueError` for non-positive weights, unknown zones, or unknown service
levels.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote – 3 kg, local zone
python -m warehouse.cli 3 local

# Express quote – 3 kg, regional zone
python -m warehouse.cli 3 regional --service express
```
