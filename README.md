# Duplicate-Finder-Algorithm
A Duplicate Finder Algorithm for Profiles

How to use the Algorithm:

1. Create a virtual environment
```
python -m venv venv
```

2. Activate the virtual environment
```
venv\Script\activate
```

3. Install fuzzywuzzy
```
pip install fuzzywuzzy
```

4. Run the Python Script using
```
python Duplicate_Finder.py
```

5. Add Test Cases and Run Again

eg:
```
  profile_1 = { "id": 1, "email": "knowkanhai@gmail.com", "first_name": "Kanhai", "last_name": "Shah", "class_year": None, "date_of_birth": None}
  profile_2 = { "id": 2, "email": "knowkanhai+donotcompare@gmail.com", "first_name": "Kanhai1", "last_name": "Shah", "class_year": "2012", "date_of_birth": "1990-10-11"}

  dup_finder(profiles=[profile_1, profile_2], fields=["first_name", "last_name"])
 ```

NOTE:
1. Duplicate Profile are getting saved into a List acting as a Database
2. Results will be printed as per the Testcase provided in the pdf
3. Python version 3+ is used
