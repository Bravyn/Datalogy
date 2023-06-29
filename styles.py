import streamlit as st

colors = {
    "dark_blue": "#000080",
    "royal_blue": "#4169E1",
    "navy_blue": "#000080",
    "dark_green": "#006400",
    "forest_green": "#228B22",
    "dark_cyan": "#008B8B",
    "dark_magenta": "#8B008B",
    "dark_purple": "#800080",
    "dark_gray": "#A9A9A9",
    "slate_gray": "#708090",
    "steel_blue": "#4682B4",
    "teal": "#008080",
    "olive": "#808000",
    "maroon": "#800000",
    "brown": "#A52A2A"
}


def format_list_with_css(items, color = colors["dark_blue"]):
    
    st.markdown(
        f"""
        <style>
            .list-item {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                
                background-color: #f2f2f2;
                color: {color};
                background-color: rgba(255, 255, 255, 0.5);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .3rem rgba(0, 0, 0, 0.3);

            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    for item in items:
        st.markdown(f'<div class="list-item">{item}</div>', unsafe_allow_html=True)

def format_title(item, color):
    
    st.markdown(
        f"""
        <style>
            .item {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                background-color: #f2f2f2;
                color: {color};
                font-weight: bold;
                background-color: rgba(5, 255, 255, 0.2);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .8rem rgba(0, 0, 0, 0.3);
                text-align: center;
                font-size: 1.618rem;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(f'<div class="item">{item}</div>', unsafe_allow_html=True)

def format_subtitle(item, color):
    
    st.markdown(
        f"""
        <style>
            .subtitle {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                background-color: #f2f2f2;
                color: {color};
                font-weight: bold;
                background-color: rgba(5, 255, 255, 0.2);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .8rem rgba(0, 0, 0, 0.3);
                text-align: center;
                font-size: 1.314rem;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(f'<div class="subtitle">{item}</div>', unsafe_allow_html=True)