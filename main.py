class Star_Cinema:

    def __init__(self) -> None:
        self.hall_list=[]


    def entry_hall(self,hall):
        self.hall_list.append(hall)

    def get_halls(self):
        return self.hall_list
    
# from browser 
class Hall(Star_Cinema):
    def __init__(self,cinema,rows,cols,hall_no):
        self.cinema=cinema
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.__seats={}
        self.__show_list=[]
        self.cinema.entry_hall(self)
    # this is command 
    # second time edit 

    def entry_show(self,show_id,movie_name):
        self.__show_list.append((show_id,movie_name))
        seat_list=[]
        
        for _ in range(self.__rows):
            row=[]
            for _ in range(self.__cols):
                row.append(0)
            seat_list.append(row)
        self.__seats[show_id]=seat_list





    def book_seats(self,show_id,seats_to_book):
        if show_id not in self.__seats:
            print("Invalid Show Id")
            raise 
        for row,col in seats_to_book:
            if row < 0 or row >= self.__rows or col<0 or col>=self.__cols:
                print("Seats position error ")
                raise
            if self.__seats[show_id][row][col]==1:
                print("already been blocked ")
                raise
            self.__seats[show_id][row][col]=1
            print(f"You booked succesfully {show_id}")
    
    def view_available_seats(self,show_id):
        if show_id not in self.__seats:
            print("Invalid show id ")
            raise
        seat_show=[]
        for row in range (self.__rows):
            row_show=[]
            for col in range(self.__cols):
                if self.__seats[show_id][row][col]==0:
                    row_show.append("0")
                else:
                    row_show.append("1")
            seat_show.append(" ".join(row_show))
        return "\n".join(seat_show)
    def view_show_list(self):
        return self.__show_list
    def hall_num(self):
        return self.__hall_no



cinema=Star_Cinema()
hall_1=Hall(cinema,5,5,1)
hall_1.entry_show(1,"Daruchini Dip")
hall_1.entry_show(2,"Dipu number 2")

while True:
    print("\n 1: View All Shows Today")
    print("\n 2: View Available seats")
    print("\n 3: Book Ticket")
    print("\n 4: Exit")
    try:
        choose=int(input("Enter Options : "))
    except ValueError:
        print("Please enter integer ")
        continue
    

    if choose==1:
        for hall in cinema.get_halls():
            for show in hall.view_show_list():
                print(f" Hall {hall.hall_num()},show id : {show[0]},Movie : {show[1]}")

    elif choose==2:
        show_id=int(input("Enter Show Id : "))
        for hall in cinema.get_halls():
            try:
                av_seat=hall.view_available_seats(show_id)
                print(f" Available seats for show id {show_id} : \n{av_seat}")
            except:
                print("Invalid")

    elif choose==3:
        show_id=int(input("Enter Show Id : "))
        num_tic=int(input("How many ticket you want : "))
        seat_to_book=[]
        for _ in range(num_tic):
            row=int(input("Enter row"))
            col=int(input("Enter col"))
            seat_to_book.append((row,col))
        try:
            for hall in cinema.get_halls():
                hall.book_seats(show_id,seat_to_book)
        except:
            pass
    elif choose==4:
        print("Exited by your choice  ")
        break
    else:
        print("Invalid option please choose 1 to 4")
