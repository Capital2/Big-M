from fastapi import status, HTTPException, Response


class BigMController():
    # def add_permission(self, permission: PermissionInSchema, db: Session):
    #     new_permission = Permission(**permission.dict())
    #     db.add(new_permission)
    #     db.commit()
    #     db.refresh(new_permission)
    #     return new_permission
    def test_method(self):
        print("test")

BigM_controller = BigMController()
