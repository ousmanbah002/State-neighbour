import streamlit as st
from google.cloud import bigquery
from  example import get_neighboring_states 




def main():
    st.title("Neighboring States Finder")
    
    state_input = st.text_input("Enter a US state name:")
    
    
    if st.button("Find Neighboring States"):
        try:
            neighbors = get_neighboring_states(state_input)
            
            st.success(f"Neighboring states of {state_input}:")
            if not neighbors:
                st.write("No neighbors found")
                st.write(f"Debug: State input was {state_input}")
            else:
        
            
                for neighbor in neighbors:
                    st.write(12)
                    st.write(neighbor)
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()