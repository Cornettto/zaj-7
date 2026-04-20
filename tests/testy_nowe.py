from src.models import Apartment, Bill, Parameters, Tenant, TenantSettlement, Transfer, ApartmentSettlement
def test_transfer_validation_extreme_values():
    manager = Manager(Parameters())
    manager.set_transfer_limits(min_value=10.0, max_value=10000.0)
    
    bad_transfer = Transfer(amount_pln=10001.0, ...) 
    errors = manager.validate_transfers([bad_transfer])
    



    
    assert len(errors) > 0
    assert "Value too high" in errors[0]