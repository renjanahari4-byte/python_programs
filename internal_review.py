print("Movie Rating and Recommendation System")
movies = ["Alamara","Athiradi","luca","Drishyam"]
geners = ("Romance","Thriller","comedy")
unique_actors = {"Mamooty","Mohanlal","Tovino Thomas"}
ratings = {"Alamara" : 7.5,"Athiradi" : 8.5,"luca" : 9.5}

print("Movie Ratings")
for movie, rating in ratings.items():
    print(f"{movie} : {rating}")
highest_rating_movie=max(ratings,key=ratings.get)
print("highest rated movie ")
print(f"{highest_rating_movie} : {ratings} ")

sorted_movies = sorted(ratings.items(),key=lambda x:x[1],reverse=True
)
print("Movies Sorted by Rating:")
for movie,rating in sorted_movies:
    print(f"{movie} : {rating}")

movie=input("enter the movie to be searched ")
if movie in movies:
    print(f"{movie} found")
else:
    print(f"{movie} notfound")

average=0
for rating in ratings.items():
    average+=rating
    average_rating=average / ratings
print("Average rating: ",average_rating)


print("Movies above average rating: ")
for rating in ratings.items():
    if rating > average_rating:
        print(f" {movie} : {rating}")

print("Recomended movies : ")
for rating in ratings.items():
    if rating>= 8.5:
        print(movie)

# College Admission Management System

for i in range(1,11):

    print("\nEnter Student",i,"Details")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))
    city = input("Enter City: ")


    # list
    student_names.append(name)


    # set
    cities.add(city)


    # dictionary
    students[name] = {
        "age": age,
        "course": course,
        "marks": marks,
        "city": city
    }
student_names = []
courses = (
    "Computer Science",
    "Commerce",
    "Mechanical",
    "Electronics"
)
cities = set()
students = {}

total = 0

for details in students.values():

    total += details["marks"]


average = total / len(students)


print("\nAverage Marks:",average)



