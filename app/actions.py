from django.contrib.auth.models import (
    User,
    Group,
    Permission
)
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from app.ui import (
    PermissionWindow,
    UserWindow
)


class UserPack(ObjectPack):
    """
        Pack for model User
    """
    model = User
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = UserWindow

    def save_row(self, obj, create_new, request, context):
        obj.set_password(obj.password)
        obj.save()


class GroupPack(ObjectPack):
    """
        Pack for model Group
    """
    model = Group
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)


class ContentTypePack(ObjectPack):
    """
        Pack for model ContentType
    """
    model = ContentType
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)


class PermissionPack(ObjectPack):
    """
        Pack for models Permission
    """
    model = Permission
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = PermissionWindow
