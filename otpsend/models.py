from django.db import models


# Create your models here.


class Insurance(models.Model):
    # plate_number = models.ForeignKey(Car_registration.plate_number, on_delete=models.CASCADE)
    # car_owner = models.ForeignKey(Car_registration.car_model, on_delete=models.CASCADE)
    # Owner_Id = models.ForeignKey(Car_registration.Owner_Id, on_delete=models.CASCADE)
    # car_model = models.ForeignKey(Car_registration.car_model, on_delete=models.CASCADE)
    # car_registration = models.ManyToManyField(Car_registration)

    insurance_status = models.BooleanField(default=False)  # if this check status is True means that car paid insurance
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Tax(models.Model):
    # car_registration = models.ManyToManyField(Car_registration)

    tax_status = models.BooleanField(default=False)
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Control(models.Model):
    # car_registration = models.ManyToManyField(Car_registration)


    control_status = models.BooleanField(default=False)
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Car_registration(models.Model):
    plate_number = models.CharField(primary_key=True, max_length=200, null=False)
    car_owner = models.CharField(max_length=200, null=False)
    Owner_Id = models.IntegerField()
    phonenumber = models.CharField(max_length=50, default=0)
    car_model = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=100, null=False)
    Time_done = models.DateTimeField(auto_now_add=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)

    def __str__(self):
        return self.plate_number
