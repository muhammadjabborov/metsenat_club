from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Sponsor, Student, University, StudentSponsor


class CreateSponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'sponsor_type', 'phone_number', 'balance', 'company_name')


class ListSponsorsSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'balance', 'spent_amount', 'register_datetime', 'status')


class DetailSponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'balance', 'status', 'company_name')


class UpdateSponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'sponsor_type', 'phone_number', 'balance', 'status', 'payment_type', 'company_name')


class CreateUniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class CreateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'student_type', 'tuition_fee')


class ListStudentsSerializer(ModelSerializer):
    university = CreateUniversitySerializer()

    class Meta:
        model = Student
        fields = ('name', 'student_type', 'university', 'received_amount', 'tuition_fee')


class StudentSponsorSerializer(ModelSerializer):
    def validate(self, data):
        if data['amount'] > data['sponsor'].balance:
            raise ValidationError({
                'amount': "The amount entered must be less than the sponsor's balance"
            })

        if data['amount'] + data['student'].received_amount > data['student'].tuition_fee:
            raise ValidationError({
                'amount': "The amount allocated to the student must be smaller than the contract amount!"
            })

        return data

    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'student', 'amount')


class UpdateStudentSponsorSerializer(ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'student', 'amount')


class DetailStudentSponsorSerializer(ModelSerializer):
    sponsor = ListSponsorsSerializer()

    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'amount')


class DetailStudentSerializer(ModelSerializer):
    university = CreateUniversitySerializer()
    sponsors = DetailStudentSponsorSerializer(many=True)

    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'student_type', 'received_amount', 'tuition_fee', 'sponsors')


class UpdateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', 'university', 'tuition_fee')


class LineDashboardStudentsSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'created_at')


class LineDashboardSponsorsSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'created_at')
