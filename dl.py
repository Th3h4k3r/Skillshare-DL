import sys, os
from skillshare import Skillshare, splash

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare("PHPSESSID=YOUR_PHPSESSID_HERE")
    course_url = sys.argv[1]
    #dl.download_course_by_url(course_url)
    dl.download_course_by_class_id(course_url)


if __name__ == "__main__":
    splash()
    main()
