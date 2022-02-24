from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,phone_number,**extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be provided")
        phone_number = self.normalize_phone_number(phone_number)
        user=self.model(phone_number=phone_number,**extra_fields)
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password):
       
        user = self.create_user(
            phone_number=self.normalize_phone_number(phone_number),
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

			
		
		
    
        
        

     
