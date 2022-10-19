from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import CultSerializer,PersSerializer,SerreSerializer
from base.models import Culture,Person,Serre 

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List Personne':'/listpers/',
        'List Serre':'/listserre/',
        'List culture':'/listcult/',

        'Create Personne':'/setpers/',
        'Create Serre':'/setserre/',
        'Create Culture':'/setcult/',

        'Update Person':'/uppers/<str:pk>',
        'Update Serre':'/upserre/<str:pk>',
        'Update Culture':'/upcult/<str:pk>',

        'Detail Person':'/dpers/<str:pk>',
        'Detail Serre':'/dserre/<str:pk>',
        'Detail Culture':'/dcult/<str:pk>',
    }
    return Response(api_urls)

#GET
@api_view(['GET'])
def getPers(request):
    persons = Person.objects.all()
    serrial = PersSerializer(persons, many=True)
    return Response(serrial.data)

@api_view(['GET'])
def getSerre(request):
    persons = Serre.objects.all()
    serrial = SerreSerializer(persons, many=True)
    return Response(serrial.data)

@api_view(['GET'])
def getCult(request):
    persons = Culture.objects.all()
    serrial = CultSerializer(persons, many=True)
    return Response(serrial.data)



#GET_ONLY
@api_view(['GET'])
def ddayPers(request,wrd):
    persons = Person.objects.get(firebaseId=wrd)
    serrial = PersSerializer(persons)
    return Response(serrial.data)

@api_view(['GET'])
def ddaySerre(request,wrd):
    persons = Serre.objects.get(hashSerre=wrd)
    serrial = SerreSerializer(persons)
    return Response(serrial.data)

@api_view(['GET'])
def ddayCult(request,pk):
    persons = Culture.objects.get(id=pk)
    serrial = CultSerializer(persons)
    return Response(serrial.data)



#SET
@api_view(['POST'])
def setPers(request):
    serrial = PersSerializer(data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['POST'])
def setSerre(request):
    serrial = SerreSerializer(data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['POST'])
def setCult(request):
    serrial = CultSerializer(data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)



#UPDATE
@api_view(['POST'])
def updPers(request,pk):
    collect = Person.objects.get(id=pk)
    serrial = PersSerializer(instance=collect,data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['POST'])
def upSerre(request,pk):
    collect = Serre.objects.get(id=pk)
    serrial = SerreSerializer(instance=collect,data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['POST'])
def updSerre(request,wrd):
    collect = Serre.objects.get(hashSerre=wrd)
    serrial = SerreSerializer(instance=collect,data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['POST'])
def updCult(request,pk):
    collect = Serre.objects.get(hashSerre=wrd)
    serrial = SerreSerializer(instance=collect,data=request.data)
    if serrial.is_valid():
        serrial.save()
    return Response(serrial.data)

@api_view(['DELETE'])
def delSerre(request,wrd):
    collect = Serre.objects.get(hashSerre=wrd)
    collect.delete()
    return Response("success")



#SEARCH
@api_view(['GET'])
def seaPers(request,wrd):
    collect = Person.objects.filter(firebaseId=wrd)
    if collect.exists():
        return Response("yep")
    else:
        return Response("nope")

@api_view(['GET'])
def seaSerre(request,wrd):
    collect = Serre.objects.filter(hashSerre=wrd)
    if collect.exists():
        return Response("okey")
    else:
        return Response("none")