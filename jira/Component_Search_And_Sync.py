from jira import JIRA

# Replace with your Jira instance URL and authentication details
jira_url = '<YOUR JIRA DOMAIN>'
username = '<YOUR JIRA MAIL ID>'
password = '<YOUR JIRA TOKEN>'

# Connect to Jira
jira = JIRA(server=jira_url, basic_auth=(username, password))

def get_components(project_key):
    """Fetch all components for a given project key."""
    project = jira.project(project_key)
    return [each_component.name for each_component in  project.components] 

def create_component_if_missing(destination_project_key, component_name):
    """Create a component in the destination project if it doesn't exist."""
    existing_component_names = get_components(destination_project_key)    
    if component_name not in existing_component_names:
        # Create the component
        jira.create_component(name=component_name, project=destination_project_key)
        print(f"Created component '{component_name}' in project '{destination_project_key}'")
    else:
        print(f"Component '{component_name}' already exists in project '{destination_project_key}'")

def sync_components(source_project_key, destination_project_key):
    """Sync components from source to destination project."""
    source_components = get_components(source_project_key)
    
    for component in source_components:
        create_component_if_missing(destination_project_key, component)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Get components from a project")
        print("2. Sync components from source to destination project")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            project_key = input("Enter the project key: ")
            print(get_components(project_key))            
        
        elif choice == '2':
            source_project_key = input("Enter the source project key: ")
            destination_project_key = input("Enter the destination project key: ")
            sync_components(source_project_key, destination_project_key)
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()            
