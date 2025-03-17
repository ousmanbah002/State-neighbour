import os
from google.cloud import bigquery
from dotenv import load_dotenv
import google.auth

# Load environment variables
load_dotenv()

# Get PROJECT_ID from environment variable
project_id = os.environ.get("PROJECT_ID")

# Debugging authentication
try:
    
    credentials, default_project = google.auth.default()
    
    
    # Create client with explicit project ID
    client = bigquery.Client(
        project=project_id or default_project, 
        credentials=credentials
    )
    
    print(f"BigQuery Client created for project: {client.project}")

except Exception as e:
    print(f"Authentication error: {e}")
    raise

def get_neighboring_states(state):
    US_STATE_ABBREVIATIONS = {
    'ALABAMA': 'AL',
    'ALASKA': 'AK',
    'ARIZONA': 'AZ',
    'ARKANSAS': 'AR',
    'CALIFORNIA': 'CA',
    'COLORADO': 'CO',
    'CONNECTICUT': 'CT',
    'DELAWARE': 'DE',
    'FLORIDA': 'FL',
    'GEORGIA': 'GA',
    'HAWAII': 'HI',
    'IDAHO': 'ID',
    'ILLINOIS': 'IL',
    'INDIANA': 'IN',
    'IOWA': 'IA',
    'KANSAS': 'KS',
    'KENTUCKY': 'KY',
    'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA',
    'MICHIGAN': 'MI',
    'MINNESOTA': 'MN',
    'MISSISSIPPI': 'MS',
    'MISSOURI': 'MO',
    'MONTANA': 'MT',
    'NEBRASKA': 'NE',
    'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH',
    'NEW JERSEY': 'NJ',
    'NEW MEXICO': 'NM',
    'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC',
    'NORTH DAKOTA': 'ND',
    'OHIO': 'OH',
    'OKLAHOMA': 'OK',
    'OREGON': 'OR',
    'PENNSYLVANIA': 'PA',
    'RHODE ISLAND': 'RI',
    'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD',
    'TENNESSEE': 'TN',
    'TEXAS': 'TX',
    'UTAH': 'UT',
    'VERMONT': 'VT',
    'VIRGINIA': 'VA',
    'WASHINGTON': 'WA',
    'WEST VIRGINIA': 'WV',
    'WISCONSIN': 'WI',
    'WYOMING': 'WY'
}

    state_abb = US_STATE_ABBREVIATIONS.get(state.upper())
    if not state_abb:
        raise ValueError(f"No abbreviation found for state: {state}")

    query = """
    SELECT neighbors_state
    FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`, 
    UNNEST(neighbors_state) as neighbors_state
    WHERE state = @state
    """

    
    try:
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("state", "STRING", state_abb)
            ]
        )
        query_job = client.query(
            query, 
            job_config=job_config,
            location='US'
        )
        
        # Fetch and print results
        results = list(query_job.result())

        neighboring_states = [row.neighbors_state for row in results]
        return neighboring_states
    
    except Exception as e:
        print(f"Query execution error: {type(e)}")
        print(f"Detailed error: {e}")
        raise