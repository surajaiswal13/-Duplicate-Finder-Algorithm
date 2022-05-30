from fuzzywuzzy import fuzz

# List acting as Database for storing Duplicate profiles
Duplicate_Profiles_Table = []

def dup_finder(profiles, fields):
  """
  Duplicate FInder Algorithm for Profiles for
  M number of profiles and N number of fields
  """

  try:  
    l = 0
    r = 1

    while r < len(profiles):
      
      # Storage for different attributes
      matching_attributes = []
      non_matching_attributes = []
      ignored_attributes = []
      flag = 1

      # For Storing total_score
      total_score = 0

      pf1_prim = profiles[l]["first_name"] + profiles[l]["last_name"] + profiles[l]["email"]
      pf2_prim = profiles[r]["first_name"] + profiles[r]["last_name"] + profiles[r]["email"]

      # Checking Ratio
      ratio = fuzz.ratio(pf1_prim, pf2_prim)

      if ratio > 80:
        total_score += 1
        flag = 0

      if flag == 0:
        if "first_name" in fields:
          fields.remove("first_name")
          matching_attributes.append("first_name")
        if "last_name" in fields:
          fields.remove("last_name")
          matching_attributes.append("last_name")
        if "email" in fields:
          fields.remove("email")
          matching_attributes.append("email")

      # Looping in fields comparing each for Profile n1 and Profile n2
      for field in fields:

        if profiles[l][field] and profiles[r][field]:

          if profiles[l][field] == profiles[r][field]:
            total_score += 1
            matching_attributes.append(field)

          else:
            total_score -= 1
            non_matching_attributes.append(field)

        else:
          ignored_attributes.append(field)

      # Adding the Remaining Attributes
      for ig_field in profile_1:
        if ig_field not in fields and ig_field != "id" and ig_field not in matching_attributes and ig_field not in non_matching_attributes:
          ignored_attributes.append(ig_field)
      
      # Adding to Duplicates table database
      if total_score > 1:
        Duplicate_Profiles_Table.append([profiles[l], profiles[r]])

      # Moving to next Database
      l += 1
      r = l+1
      
    print(f"Total Matching Score: {total_score}, Matching Attributes:{matching_attributes}, Non Matching Attributes: {non_matching_attributes}, Ignored Attributes: {ignored_attributes}")

  except Exception as e:
    print(e)



# TESTCASES

# ------ TestCase 1: -------

# profile_1 = { "id": 1, "email": "knowkanhai@gmail.com", "first_name": "Kanhai", "last_name": "Shah", "class_year": "2012",
#              "date_of_birth": "1990-10-11" }
# profile_2 = { "id": 2, "email": "knowkanhai@gmail.com", "first_name": "Kanhai1", "last_name": "Shah", "class_year": "2012", 
#              "date_of_birth": "1990-10-11"}


# dup_finder(profiles = [profile_1, profile_2], fields =["email","first_name","last_name", "class_year", "date_of_birth"])

# ------ TestCase 2: -------

# profile_1 = { "id": 1, "email": "knowkanhai@gmail.com", "first_name": "Kanhai", "last_name": "Shah", "class_year": None, "date_of_birth": None}
# profile_2 = { "id": 2, "email": "knowkanhai@gmail.com", "first_name": "Kanhai1", "last_name": "Shah", "class_year": "2012", "date_of_birth": "1990-10-11"}


# dup_finder(profiles= [profile_1, profile_2], fields=["email", "first_name", "last_name", "class_year", "date_of_birth"])

# ------ TestCase 3: -------

# profile_1 = { "id": 1, "email": "knowkanhai@gmail.com", "first_name": "Kanhai", "last_name": "Shah", "class_year": None, "date_of_birth": None}
# profile_2 = { "id": 2, "email": "knowkanhai+donotcompare@gmail.com", "first_name": "Kanhai1", "last_name": "Shah", "class_year": "2012", "date_of_birth": "1990-10-11"}

# dup_finder(profiles=[profile_1, profile_2], fields=["first_name", "last_name"])