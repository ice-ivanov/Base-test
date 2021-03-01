from rest_framework import serializers

from .models import User, UserRole


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.ReadOnlyField(source='role.name')

    class Meta:
        model = User
        fields = ['id', 'username', 'notifications', 'role_name']

    def validate_user_role(self, role, new_role):
        """
        Checks if user role already exists.
        IMO completely unnecessary, since without validation,
        in case such role already exists, it just uses that role.
        """
        if new_role:
            if UserRole.objects.filter(name=role):
                raise serializers.ValidationError({'role': 'This role already exists.'})
            else:
                UserRole(name=role).save()
                return UserRole.objects.filter(name=role).first()
        else:
            return UserRole.objects.filter(id=role).first()

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            notifications=validated_data['notifications'],
        )
        user.role = self.validate_user_role(self.initial_data['role'], self.initial_data['new_role'])
        user.save()
        return user

    def update(self, request, *args):
        user = User.objects.filter(pk=request.id).first()
        user.username = args[0]['username']
        user.notifications = args[0]['notifications']
        user.role = self.validate_user_role(self.initial_data['role'], self.initial_data['new_role'])
        user.save()
        return user


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name']
