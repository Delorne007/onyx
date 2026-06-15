from connector import JiraServiceManagementConnector

# Initialize the connector
connector = JiraServiceManagementConnector(
    jira_url="https://YOUR_DOMAIN.atlassian.net",
    jira_user_email="YOUR_EMAIL@example.com",
    jira_api_token="YOUR_API_TOKEN",
    service_desk_id="" # Leave blank to test discovery
)

try:
    # 1. Test Discovery
    desks = connector._get_service_desks()
    print(f"Successfully discovered {len(desks)} service desks: {desks}")
    
    if desks:
        # 2. Test Request Fetching (first batch)
        print("Fetching requests for the first desk...")
        request_gen = connector._get_customer_requests(desks[0], start_time=0)
        batch = next(request_gen, [])
        print(f"Successfully fetched {len(batch)} requests from desk {desks[0]}")
        
except Exception as e:
    print(f"Test failed with error: {e}")
