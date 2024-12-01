mkdir -p ~/.streamlit/

each "\
[server]\n\
port = $PORT\n\
ENABLEcors = false\n\
headless = true\n\
\n\
" > ~/.streamliy/config.toml