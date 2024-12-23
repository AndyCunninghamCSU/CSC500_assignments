# Andrew Cunningham
# CSC500 - Critical Thinking Assignment 7

class CourseInfo:
    '''
    creates ditionaries:
        room_number = {(course_number, room_number)}
        instructor = {(course_number, instructor)}
        meeting_time = {(course_number, meeting_time)}
    
    functions:
        get_info(course_number: String) -> [room_number, instructor, meeting time]
    '''

    def __init__(self):
        self.room_number = {
            "CSC101":"3004",
            "CSC102":"4501",
            "CSC103":"6755",
            "NET110":"1244",
            "COM241":"1411"
        }

        self.instructor = {
            "CSC101":"Haynes",
            "CSC102":"Alvarado",
            "CSC103":"Rich",
            "NET110":"Burke",
            "COM241":"Lee"
        }

        self.meeting_time = {
            "CSC101":"8:00 a.m.",
            "CSC102":"9:00 a.m.",
            "CSC103":"10:00 a.m.",
            "NET110":"11:00 a.m.",
            "COM241":"1:00 p.m."
        }

    def get_info(self, course_number: str):
        ''' returns an array containing the dictionary info for course_number '''
        result = []
        result.append(self.room_number.get(course_number))
        result.append(self.instructor.get(course_number))
        result.append(self.meeting_time.get(course_number))

        return result

    def course_exists(self, course_number: str):
        '''
        returns if key is in room_number
        assumes that all the keys for all 3 dicts are the same
        '''
        return course_number in self.room_number

def main():
    course_info = CourseInfo()
    print("Course Lookup! - q to exit")
    while True:
        course_number = input("Course Number: ")
        if (course_number == 'q'):
            return
        else:
            if not course_info.course_exists(course_number):
                print(f"{course_number} Does not exist, try again!")
            else:
                items = course_info.get_info(course_number)
                print(f"Course: {course_number}, Room number: {items[0]}, Instructor: {items[1]}, Meeting Time: {items[2]}")

if __name__ == '__main__':
    main()