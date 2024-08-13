from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def list_person(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from people_person")
        persons = dictfetchall(cursor)

    return Response(persons)


@api_view(['GET'])
def view_person(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from people_person WHERE id = %s", [id])
        persons = dictfetchall(cursor)

    return Response(persons)


@api_view(['POST'])
def add_person(request):
 
    with connection.cursor() as cursor:
        name = request.data.get('name')
        views = request.data.get('views')
        type = request.data.get('type')
        
        cursor.execute("INSERT INTO people_person (name, views, type) VALUES(%s, %s, %s)", [name, views, type])
        

    return Response({"name": name, "views": views, "type": type}, status=status.HTTP_201_CREATED)
        

@api_view(['PUT'])
def update_person(request, id):
    with connection.cursor() as cursor:
        if not person_exists(id, cursor):
                return Response("Person with given id does not exist.", status=status.HTTP_400_BAD_REQUEST)
              
        name = request.data.get('name')
        views = request.data.get('views')
        type = request.data.get('type')
      
        cursor.execute("UPDATE people_person SET name = %s, views = %s, type = %s WHERE id = %s", [name, views, type, id])

    return Response({"name": name, "views": views, "type": type})


@api_view(['DELETE'])
def delete_person(request, id):
    with connection.cursor() as cursor:
        if not person_exists(id, cursor):
                return Response("Person with given id does not exist.", status=status.HTTP_400_BAD_REQUEST)
            
        cursor.execute("DELETE FROM people_person WHERE id = %s", [id])

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def person_type(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT type, SUM(views) as views FROM people_person GROUP BY type")
        types = dictfetchall(cursor)
        
    return Response(types)


def person_exists(id, cursor):
    cursor.execute("SELECT id from people_person WHERE id = %s", [id])
    if cursor.rowcount:
        return True
        
    return False


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
