from rest_framework import viewsets, permissions
from api.serializers import *


class InventoryViewSet(viewsets.ModelViewSet):
    """
    处理  GET POST , 处理 /api/post/<pk>/ GET PUT PATCH DELETE
    """
    queryset = AnsibleInventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAdminUser,)


class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all().order_by('id')
    serializer_class = AssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class ServerAssetsViewSet(viewsets.ModelViewSet):
    queryset = ServerAssets.objects.all().order_by('id')
    serializer_class = ServerAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class NetworkAssetsViewSet(viewsets.ModelViewSet):
    queryset = NetworkAssets.objects.all().order_by('id')
    serializer_class = NetworkAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class OfficeAssetsViewSet(viewsets.ModelViewSet):
    queryset = OfficeAssets.objects.all().order_by('id')
    serializer_class = OfficeAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class SecurityAssetsViewSet(viewsets.ModelViewSet):
    queryset = SecurityAssets.objects.all().order_by('id')
    serializer_class = SecurityAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class StorageAssetsViewSet(viewsets.ModelViewSet):
    queryset = StorageAssets.objects.all().order_by('id')
    serializer_class = StorageAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class SoftwareAssetsViewSet(viewsets.ModelViewSet):
    queryset = SoftwareAssets.objects.all().order_by('id')
    serializer_class = SoftwareAssetsSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProjectConfigViewSet(viewsets.ModelViewSet):
    queryset = ProjectConfig.objects.all().order_by('id')
    serializer_class = ProjectConfigSerializer
    permission_classes = (permissions.IsAdminUser,)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAdminUser,)


class AssetProviderViewSet(viewsets.ModelViewSet):
    queryset = AssetProvider.objects.all().order_by('id')
    serializer_class = AssetProviderSerializer
    permission_classes = (permissions.IsAdminUser,)


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all().order_by('id')
    serializer_class = IDCSerializer
    permission_classes = (permissions.IsAdminUser,)


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all().order_by('id')
    serializer_class = CabinetSerializer
    permission_classes = (permissions.IsAdminUser,)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAdminUser,)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer
    permission_classes = (permissions.IsAdminUser,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAdminUser,)


class FortViewSet(viewsets.ModelViewSet):
    queryset = FortServer.objects.all().order_by('id')
    serializer_class = FortSerializer
    permission_classes = (permissions.IsAdminUser,)


class FortUserViewSet(viewsets.ModelViewSet):
    queryset = FortServerUser.objects.all().order_by('id')
    serializer_class = FortUserSerializer
    permission_classes = (permissions.IsAdminUser,)


class PeriodicTaskViewSet(viewsets.ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    permission_classes = (permissions.IsAdminUser,)


class WebSiteViewSet(viewsets.ModelViewSet):
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer
    permission_classes = (permissions.IsAdminUser,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser,)
