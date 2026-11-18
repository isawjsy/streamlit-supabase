import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests
import docker
import subprocess
import platform
import distro

r =requests.get(f'https://docs.google.com/spreadsheet/ccc?key=1ORu0GIhEBfyEtUr9GGFtSg_0QaxB2LuHEvxSpgSaZQs&output=csv')
open('dataset.csv', 'wb').write(r.content)
feedback_df = pd.read_csv('dataset.csv')

def is_docker_installed():
    try:
        subprocess.check_output(["docker", "--version"])
        return True
    except FileNotFoundError:
        return False

# Set page title and favicon to an emoji
st.set_page_config(page_title="Streamlit App", page_icon="🚀")

def main():
    st.title('Streamlit App 🚀')

    # README Documentation Expander
    with st.expander("README Documentation 📝"):
        with open("README.md", "r") as readme_file:
            readme_content = readme_file.read()
        st.write("")
        st.markdown(readme_content)
        os_platform = platform.system()
        distribution_info = distro.linux_distribution(full_distribution_name=False)
        if is_docker_installed():
            st.write(f"The operating system is: {os_platform} of distribution: {distribution_info[0]} {distribution_info[1]} with Docker installed 🐳")
        else:
            st.write(f"The operating system is: {os_platform} of distribution: {distribution_info[0]} {distribution_info[1]} without Docker installed 🐳")

    # Show the author content
    author_expander = st.expander("Author's Gthub Projects 🌏")
    with author_expander:
        url = "https://raw.githubusercontent.com/mattmajestic/mattmajestic/main/README.md"
        response = requests.get(url)
        readme_content = response.text if response.status_code == 200 else ""
        iframe_html = f'<iframe srcdoc="{readme_content}</iframe>'
        st.markdown(iframe_html, unsafe_allow_html=True)

        # Show the BTC Pay Server
    btc_expander = st.expander("Donate BTC 💸")
    with btc_expander:
        url = "https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC"
        link='Pay wit BTC [via this link](https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC)'
        st.markdown(link,unsafe_allow_html=True)
        components.iframe(url,width = 300,height = 500, scrolling=True)
    feedback_expander = st.expander("Give Feedback 🤝")
    with feedback_expander:
        st.dataframe(feedback_df)
        st.markdown('''<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfkcEBiOklswShRGok5hjJQ1UTuGcT-ZB-6gBx6ehLCjlrRIQ/viewform?embedded=true" width="640" height="2197" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>''', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
