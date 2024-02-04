import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    with open('mm.txt') as f:
       lines = f.readlines()
    d = [i.strip() for i in lines]
    for i in d:
      st.text(i)

    
    if button := st.button("press"):
      d += ["Hello"]
      with open('mm.txt','w') as f:
         f.truncate()
         for i in d:
            f.write(f"{i}\n")

    with open('mm.txt') as f:
       lines = f.readlines()
    d = [i.strip() for i in lines]
    for i in d:
      st.text(i)



if __name__ == "__main__":
    run()
