# school_data.py
# Ashim Orko
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# You may add your own additional classes, functions, variables, etc.

years_data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

school_names = ["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", 
                    "Forest Lawn High School", "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", 
                    "James Fowler High School", "Ernest Manning High School", "William Aberhart High School", "National Sport School", 
                    "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", 
                    "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"]

school_codes = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 9860, 9865]

years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

grades = ["Grade 10", "Grade 11", "Grade 12"]

num_schools = len(school_names)

num_grades = len(grades)

num_years = len(years)

# Initialize a 3D numpy array to store enrollment data
enrollment_data = np.zeros((num_schools, num_grades, num_years))

# Populate the enrollment_data array with the given data for each year
for year_index, year in enumerate(years_data):
    enrollment_data[:, :, year_index] = year.reshape((num_schools, num_grades))


def get_school(school_input):
    """
    Get the index of a school based on its name or code.

    Parameters:
    - school_input (str or int): Name or code of the school.

    Returns:
    - int: Index of the school in the school_names or school_codes list.

    Raises:
    - ValueError: If the provided input is not a valid school name or code.
    """
    # Check if the input is a string
    if (type(school_input) == str):
        # Check if the school name exists in the list of school names
        if school_input in school_names:
            return school_names.index(school_input)
        else:
            # Raise an error if the school name is not found
            raise ValueError("Please enter a valid school name or code.")
    # Check if the input is an integer 
    elif (type(school_input) == int):
        # Check if the school code exists in the list of school codes
        if school_input in school_codes:
            return school_codes.index(school_input)
        else:
            # Raise an error if the school code is not found
            raise ValueError("Please enter a valid school name or code.")
    else:
        # Raise an error if the input is neither a string nor an integer
        raise ValueError("Please enter a valid school name or code.")

def median_enrollment_over_500(school_input, enrollment_data):
    """
    Calculate the median enrollment for a given school that exceeds 500.

    Parameters:
    - school_input (str or int): Name or code of the school.
    - enrollment_data (numpy.ndarray): 3D array containing enrollment data for all schools, grades, and years.

    Returns:
    - None

    """

    # Get the index of the school
    school_index = get_school(school_input)

    # Extract enrollment data for the specified school
    school_enrollment = enrollment_data[school_index]

    # Filter enrollments over 500
    enrollments_over_500 = school_enrollment[school_enrollment > 500]

    # Check if there are enrollments over 500 and calculate median
    if len(enrollments_over_500) == 0:
        print("No enrollments over 500.")
    else:
        median_enrollment = int(np.floor(np.median(enrollments_over_500)))
        print(f"For all enrollments over 500, the median value was: {median_enrollment}")


    
def calculate_school_stats(school_index):
    """
    Calculate statistics for a specific school.

    Parameters:
    - school_index (int): Index of the school.

    Returns:
    - dict: A dictionary containing various statistics for the specified school.
    """
    # Initialize an empty dictionary to store school statistics
    school_stats = {}

    # Extract enrollment data for the specified school
    school_enrollment = enrollment_data[school_index]

    # Calculate data required for Stage 2
    school_stats['mean_grade_10'] = int(np.nanmean(school_enrollment[0, :]))
    
    school_stats['mean_grade_11'] = int(np.nanmean(school_enrollment[1, :]))
    
    school_stats['mean_grade_12'] = int(np.nanmean(school_enrollment[2, :]))

    school_stats['highest_enrollment'] = int(np.nanmax(school_enrollment)) 
    
    school_stats['lowest_enrollment'] = int(np.nanmin(school_enrollment))

    school_stats['yearly_enrollments'] = {year: int(np.nansum(school_enrollment[:, i])) for i, year in enumerate(years)}

    total_enrollment_per_year = np.nansum(school_enrollment, axis = 0)
    
    school_stats['total_enrollment_10_years'] = int(np.nansum(total_enrollment_per_year))
    
    school_stats['mean_total_yearly_enrollment'] = int(np.nanmean(total_enrollment_per_year))
    
    return school_stats

def calculate_general_statistics():
    """
    Calculate general statistics for all schools.

    Returns:
    - dict: A dictionary containing various general statistics.
    """
    
    # Initialize an empty dictionary to store general statistics
    general_stats = {}

    # Calculate data required for Stage 3
    general_stats['mean_enrollment_2013'] = int(np.floor(enrollment_data[:, :, 0].mean()))

    masked_enrollment_2022 = np.ma.masked_invalid(enrollment_data[:, :, -1])
    
    general_stats['mean_enrollment_2022'] = int(np.floor(masked_enrollment_2022.mean()))
    
    general_stats['total_enrollment_2022'] = int(np.nansum(masked_enrollment_2022))
    
    general_stats['highest_yearly_enrollment'] = int(np.nanmax(enrollment_data))
    
    general_stats['lowest_yearly_enrollment'] = int(np.nanmin(enrollment_data))

    return general_stats
    

def main():
    """
    Main function to display school enrollment statistics.

    Returns:
    - None
    """
    
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array:", enrollment_data.shape)
    print("Dimensions of full data array:", enrollment_data.ndim)

   
    # Prompt for user input
    while True:
        school_input = input("Please enter the highschool name or school code: ")
    
        try:
            # Attempt to convert input to integer if it's not already
            school_input = int(school_input)
        except ValueError:
            # Pass if input is already an integer
            pass

        try:
            # Get the index of the school based on input
            school_index = get_school(school_input)
            school_name = school_names[school_index]
            school_code = school_codes[school_index]
            break
        except ValueError as e:
            # Handle invalid input errors
            print(e)

    # Calculate statistics for the selected school for Stage 2
    school_stats = calculate_school_stats(school_index)
            
     
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code} ")
    print("Mean enrollment for Grade 10:", school_stats['mean_grade_10'])
    print("Mean enrollment for Grade 11:", school_stats['mean_grade_11'])
    print("Mean enrollment for Grade 12:", school_stats['mean_grade_12'])
    print("Highest enrollment for a single grade:", school_stats['highest_enrollment'])
    print("Lowest enrollment for a single grade:", school_stats['lowest_enrollment'])
    for year, total_enrollment in school_stats['yearly_enrollments'].items():
        print(f"Total enrollment for {year}: {int(total_enrollment)}")
    print("Total ten year enrolment:", school_stats['total_enrollment_10_years'])
    print("Mean total enrollment over 10 years:", school_stats['mean_total_yearly_enrollment'])
    median_enrollment_over_500(school_input, enrollment_data)

    # Print Stage 3 requirements here
    
    # Calculate general statistics for all schools for Stage 3
    general_stats = calculate_general_statistics()
    
    print("\n***General Statistics for All Schools***\n")
    print("Mean enrollment in 2013:", general_stats['mean_enrollment_2013'])
    print("Mean enrollment in 2022:", general_stats['mean_enrollment_2022'])
    print("Total graduating class of 2022:", general_stats['total_enrollment_2022'])
    print("Highest enrollment for a single grade:", general_stats['highest_yearly_enrollment'])
    print("Lowest enrollment for a single grade:", general_stats['lowest_yearly_enrollment'])

if __name__ == '__main__':
    main()

