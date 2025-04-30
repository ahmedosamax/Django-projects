from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import project, Reviews,tag


@api_view(['GET'])
def getRoutes(request):
    routes = [
      {'GET':'/api/projects'},
      {'GET':'/api/projects/id'},
      {'POST':'/api/projects/id/vote'},
      {'POST':'/api/users/token'},
      {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
def getProjects(request):
   projects = project.objects.all()
   serializer = ProjectSerializer(projects,many = True)
   return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
   projectt = project.objects.get(id = pk )
   serializer = ProjectSerializer(projectt,many = False)
   return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
   projectr = project.objects.get(id = pk)
   user = request.user.profile
   data = request.data
   review ,created = Reviews.objects.get_or_create(
      owner = user,
      Project = projectr, 
   )
   review.Value = data['Value']
   review.save()
   projectr.getVoteCount
   serializer = ProjectSerializer(projectr,many = False)
   print ('DATA:',data)
   return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
   tagId = request.data['tag']
   projectId = request.data['project']

   projectt = project.objects.get(id = projectId)
   tagg = tag.objects.get(id = tagId)

   projectt.Tags.remove(tagg)
   return Response('Tag was deleted!')