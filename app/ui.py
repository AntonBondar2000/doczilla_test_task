from django.contrib.contenttypes.models import ContentType
from m3_ext.ui.fields import (
    ExtStringField,
    ExtComboBox,
    BaseExtTriggerField,
    ExtCheckBox, ExtDateField
)
from m3_ext.ui.misc import ExtDataStore
from objectpack.ui import BaseEditWindow


class PermissionWindow(BaseEditWindow):
    """
        Window for Permission
    """
    def _init_components(self):
        super(PermissionWindow, self)._init_components()

        self.field__name = ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        self.field__codename = ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

        self.field__content_type = ExtComboBox(
            label=u'content_type',
            display_field='type',
            name='content_type_id',
            anchor='100%',
            editable=False,
            value_field='id',
            allow_blank=False
        )
        self.field__content_type.store = ExtDataStore(
            data=ContentType.objects.all().values_list('id', 'app_label')
        )
        self.field__content_type.trigger_action = BaseExtTriggerField.ALL

    def _do_layout(self):
        super(PermissionWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))


class UserWindow(BaseEditWindow):
    """
        Window for User
    """
    def _init_components(self):
        super(UserWindow, self)._init_components()

        self.field__username = ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field__password = ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )
        self.field__email = ExtStringField(
            label=u'email',
            name='email',
            allow_blank=False,
            anchor='100%',
            regex='.+@.+\..+',
            regex_text=u'Incorrectly email'
        )
        self.field__first_name = ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=True,
            anchor='100%'
        )
        self.field__last_name = ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=True,
            anchor='100%'
        )
        self.field__is_superuser = ExtCheckBox(
            label=u'is superuser',
            name='is_superuser',
            allow_blank=True,
            anchor='100%'
        )
        self.field__is_staff = ExtCheckBox(
            label=u'is staff',
            name='is_staff',
            allow_blank=True,
            anchor='100%'
        )
        self.field__active = ExtCheckBox(
            label=u'active',
            name='active',
            allow_blank=True,
            anchor='100%'
        )
        self.field__last_login = ExtDateField(
            label=u'last login',
            name='last_login',
            allow_blank=True,
            anchor='100%',
            format='d.m.Y'
        )
        self.field__date_join = ExtDateField(
            label=u'date joined',
            name='date_joined',
            allow_blank=True,
            anchor='100%',
            format='d.m.Y'
        )

    def _do_layout(self):
        super(UserWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__active,
            self.field__last_login,
            self.field__date_join
        ))
