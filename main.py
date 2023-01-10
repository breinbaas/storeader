import streamlit as st

uploaded_files = st.file_uploader(
    "Upload your .sto file(s)",
    type=["sto"],
    accept_multiple_files=True,
    help="Upload the sto files to get the calculated FOS",
)

for uploaded_file in uploaded_files:
    data = uploaded_file.read().decode(errors="ignore")

    fmin = "unknown (check manually)"
    method = ""
    for line in data.split("\n"):
        if (
            line.find("Information on the critical circle") > -1
            or line.find("Information on the critical plane") > -1
        ):
            fmin = line.split(":")[1].strip()
        elif line.find("Calculation method used") > -1:
            method = line.split(":")[1].strip()

    st.write("filename:", uploaded_file.name)
    st.write("method: ", method)
    st.write("FOS: ", fmin)
    st.write("-" * 80)
    # st.write(data)
