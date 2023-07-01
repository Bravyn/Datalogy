import streamlit as st
st.markdown("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bacasime+Antique&family=Belanosima:wght@400;700&family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,700;1,100;1,200&display=swap" rel="stylesheet">""",
unsafe_allow_html=True)

fonts = """
font-family: 'Bacasime Antique', serif;
font-family: 'Belanosima', sans-serif;
font-family: 'Kanit', sans-serif;
"""
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


def format_list_with_css(items, card_type = "list-item", color = colors["dark_blue"]):
    
    st.markdown(
        f"""
        <style>
            .{card_type} {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                font-family: 'Kanit', sans-serif;
                font-weight: 300;
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
        st.markdown(f'<div class={card_type}>{item}</div>', unsafe_allow_html=True)

def format_title(item, color):
    
    st.markdown(
        f"""
        <style>
            .item {{
               
                padding: .618rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                background-color: #f2f2f2;
                color: {color};
                font-weight: 700;
                background-color: rgba(5, 255, 255, 0.2);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .8rem rgba(0, 0, 0, 0.3);
                text-align: center;
                font-size: 1.618rem;
                font-family: 'Belanosima', sans-serif;
                letter-spacing: .618rem;
    
            }}
            .item:hover{{
                transform: rotate(.618deg)
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
                font-family: 'Belanosima', sans-serif;
                background-color: rgba(5, 255, 255, 0.2);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .8rem rgba(0, 0, 0, 0.3);
                text-align: center;
                font-size: 1.314rem;
                letter-spacing:.3rem
            }}
            .subtitle:hover{{
                transform: rotate(.618deg)
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(f'<div class="subtitle">{item}</div>', unsafe_allow_html=True)