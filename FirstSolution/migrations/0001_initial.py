# Generated by Django 2.0.5 on 2018-05-24 02:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SCZ_Department',
            fields=[
                ('DepartmentId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('DepartmentName', models.CharField(max_length=50)),
                ('ParentId', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_Menu',
            fields=[
                ('MenuId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('ParentId', models.CharField(max_length=50)),
                ('MenuKey', models.CharField(max_length=50)),
                ('URL', models.CharField(max_length=50)),
                ('MenuType', models.CharField(max_length=50)),
                ('Sort', models.IntegerField()),
                ('ShowCss', models.CharField(max_length=50)),
                ('ShowPIC', models.CharField(max_length=50)),
                ('CreateUser', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_Parameter',
            fields=[
                ('ParamaterId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('PName', models.CharField(max_length=50)),
                ('PValue', models.CharField(max_length=50)),
                ('ParentId', models.CharField(max_length=50)),
                ('Sort', models.IntegerField()),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_Role',
            fields=[
                ('RoleId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('RoleName', models.CharField(max_length=50)),
                ('Description', models.CharField(blank=True, max_length=150)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField()),
                ('Attribute1', models.CharField(max_length=150)),
                ('Attribute2', models.CharField(max_length=150)),
                ('Attribute3', models.CharField(max_length=150)),
                ('Attribute4', models.CharField(max_length=150)),
                ('Attribute5', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_RolePermit',
            fields=[
                ('RolePermitId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('RoleId', models.CharField(max_length=50)),
                ('MenuId', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_User',
            fields=[
                ('UserId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('LoginName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('RealName', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(blank=True, max_length=50)),
                ('TelNumber', models.CharField(blank=True, max_length=50)),
                ('Email', models.EmailField(blank=True, max_length=50)),
                ('Address', models.CharField(blank=True, max_length=150)),
                ('Description', models.CharField(blank=True, max_length=150)),
                ('DefaultURL', models.CharField(blank=True, max_length=150)),
                ('Status', models.IntegerField()),
                ('Logontimes', models.IntegerField()),
                ('Lastlogontime', models.DateTimeField(auto_now_add=True)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_UserDepartment',
            fields=[
                ('UserDepartmentId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
                ('DepartmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstSolution.SCZ_Department')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstSolution.SCZ_User')),
            ],
        ),
        migrations.CreateModel(
            name='SCZ_UserRole',
            fields=[
                ('UserRoleId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('CreateUser', models.CharField(max_length=50)),
                ('LaseWriteTime', models.DateTimeField(blank=True)),
                ('LaseWriteUser', models.CharField(blank=True, max_length=50)),
                ('IsDeleted', models.BooleanField(default='0')),
                ('Attribute1', models.CharField(blank=True, max_length=150)),
                ('Attribute2', models.CharField(blank=True, max_length=150)),
                ('Attribute3', models.CharField(blank=True, max_length=150)),
                ('Attribute4', models.CharField(blank=True, max_length=150)),
                ('Attribute5', models.CharField(blank=True, max_length=150)),
                ('RoleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstSolution.SCZ_Role')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstSolution.SCZ_User')),
            ],
        ),
    ]