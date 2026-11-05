"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0
_VALID_ZONES = {"local", "regional"}
_VALID_SERVICES = {"standard", "express"}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone – ``"local"`` or ``"regional"``.
        service: Service level – ``"standard"`` (default) or ``"express"``.
            Express adds a flat $7 surcharge on top of the standard rate.

    Returns:
        Total shipping cost rounded to two decimal places.

    Raises:
        ValueError: If *weight_kg* is not positive, *zone* is unknown, or
            *service* is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _VALID_ZONES:
        raise ValueError("unknown zone")
    if service not in _VALID_SERVICES:
        raise ValueError(f"unknown service: {service!r}; choose from {sorted(_VALID_SERVICES)}")
    base = 5.0 if zone == "local" else 8.0
    quote = round(base + 1.5 * weight_kg, 2)
    if service == "express":
        quote = round(quote + _EXPRESS_SURCHARGE, 2)
    return quote
