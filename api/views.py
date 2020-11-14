
from rest_framework import status
from rest_framework.decorators import api_view
from .ImageToText.PdfToWord import PdfToWordExample
from rest_framework.response import Response



@api_view(['POST'])
def ImageToText(request):
	try:
		uploaded_file = request.FILES['photo'].read()

		pdfToword = PdfToWordExample(uploaded_file)
		res = {

			'response': pdfToword.RunProject()
		}

		return Response(res, status=status.HTTP_200_OK)
	except Exception as i:
		return Response(i, status=status.HTTP_204_NO_CONTENT)



'''

	
	from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from .PdfToWord import PdfToWordExample
from rest_framework.generics import CreateAPIView

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List': '/task-list/',
		'Detail View': '/task-detail/<str:pk>/',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>/',
		'Delete': '/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	print("taskList : ", request)
	serializer = TaskSerializer(tasks, context={"request": request},many=True)



	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, context={"request": request})

	pdfToword = PdfToWordExample(serializer.get_photo_url(tasks))


	res =  {

		'sonuc':pdfToword.RunProject()
	}
	return Response(res)

@api_view(['POST'])
def taskCreate(request):
	print("taskCreate Çalıştı")
	print("CREATE : ", request.data)

	form = Task(request.POST, request.FILES)
	print("IMAGE : ", form)
	serializer = TaskSerializer(data=request.data, context={"request": request})


	if serializer.is_valid():
		serializer.save()



	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)



	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
'''

