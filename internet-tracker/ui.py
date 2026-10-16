
import streamlit as st
import json

with open("applications.json", "r") as file:
    applications = json.load(file)

st.set_page_config(
    page_title="Internship Tracker",
    page_icon="💼",
    layout="wide"
)

if st.session_state.get("update_success", False):
    st.success("Application updated successfully!")

st.title("💼 My Internship Tracker")
st.write("Track, organise, and manage your internship applications.")

st.divider()

st.subheader("Your Dashboard")

col1, col2, col3 = st.columns(3)

internship_number = 0
applied_number = 0

total_applications = len(applications)
for app in applications:
    if app["Status"] == "Interested":
        internship_number += 1
    elif app["Status"] == "Applied":
        applied_number += 1 


col1.metric("Total Applications", total_applications)
col2.metric("Applied", applied_number)
col3.metric("Interested", internship_number)

st.divider()
st.subheader("➕ Add a New Application")
company_name = st.text_input("Company Name")
role_name = st.text_input("Role")
status = st.selectbox(
    "Application Status",
    ["Interested", "Applied", "Interview", "Rejected", "Selected"]
)
if st.button("Add Application"):
    new_application = {
        "Company_Name": company_name,
        "Role": role_name,
        "Status": status
    }

    applications.append(new_application)

    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)

    st.success("Application added successfully!")
    st.rerun()


st.subheader("📋 Your Applications")
selected_status = st.selectbox(
    "Filter by Status",
    ["All", "Interested", "Applied", "Interview", "Rejected", "Selected"]
)

if selected_status == "All":
    filtered_applications = applications
else:
    filtered_applications = [
        app for app in applications
        if app["Status"] == selected_status
    ]

st.dataframe(
    filtered_applications,
    use_container_width=True,
    hide_index=True
)

st.divider()
st.subheader("🗑️ Delete Application")
if applications:
    company_to_delete = st.selectbox(
        "Choose an application",
        applications,
        format_func=lambda app: f"{app['Company_Name']} - {app['Role']}"
    )
if st.button("Delete Application"):
    applications.remove(company_to_delete)

    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)

    st.success("Application deleted successfully")
    st.rerun()





st.divider()
st.subheader("✏️ Update an Application")

if applications:
    selected_app = st.selectbox(
        "Select application",
        range(len(applications)),
        format_func=lambda i: (
            f"{applications[i]['Company_Name']} - "
            f"{applications[i]['Role']}"
        ),
        key="update_selection"
    )

    app = applications[selected_app]

    with st.form("update_form"):
        company = st.text_input(
            "Company Name",
            value=app["Company_Name"]
        )

        role = st.text_input(
            "Role",
            value=app["Role"]
        )

        statuses = [
            "Interested", "Applied", "Interview",
            "Rejected", "Selected"
        ]

        status = st.selectbox(
            "Status",
            statuses,
            index=statuses.index(app["Status"])
        )

        submitted = st.form_submit_button("Update Application")

    if submitted:
        applications[selected_app]["Company_Name"] = company
        applications[selected_app]["Role"] = role
        applications[selected_app]["Status"] = status

        with open("applications.json", "w") as file:
            json.dump(applications, file, indent=4)

        st.success("Application updated successfully!")
        st.rerun()
        
else:
    st.info("Add an application before updating it.")
