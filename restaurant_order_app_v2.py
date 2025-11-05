import streamlit as st

st.title("🍜 Restaurant Food Ordering Program")

st.write("Enter your current inventory below and click **Calculate Order**.")

# Tofu box
tofu = st.number_input("Tofu boxes currently in stock:", min_value=0, value=0)
tofu_order = max(0, 2 - tofu)

# Chicken boxes
st.subheader("Chicken Stock")

main_freezer = st.selectbox(
    "How much chicken is in the main freezer?",
    ["a lot", "not a lot"]
)
small_freezer = st.radio("Is the small freezer restocked with chicken?", ["yes", "no"])

# New chicken ordering logic
if main_freezer == "a lot":
    chicken_order = 25
else:
    chicken_order = 35

if small_freezer == "no":
    chicken_order += 10

# Liquid egg
liquid_egg = st.number_input("Liquid egg boxes currently in stock:", min_value=0, value=0)
egg_order = max(0, 3 - liquid_egg)

# Scallion pancakes
scallion_pancake = st.number_input("Scallion pancake boxes currently in stock:", min_value=0, value=0)
pancake_order = max(0, 2 - scallion_pancake)

# Lo mein
lo_mein = st.number_input("Lo mein boxes currently in stock:", min_value=0, value=0)
lo_mein_order = max(0, 4 - lo_mein)

# Cooking wine
cooking_wine = st.number_input("Cooking wine jugs currently in stock:", min_value=0, value=0)
cooking_wine_order = 1 if cooking_wine <= 3 else 0

# Edamame pods
edamame = st.number_input("Edamame pod boxes currently in stock:", min_value=0, value=0)
edamame_order = max(0, 3 - edamame)

# Degreaser concentrate
degreaser = st.number_input("Degreaser jugs currently in stock:", min_value=0, value=0)
degreaser_order = 1 if degreaser < 1 else 0

# Frozen shrimp
shrimp = st.number_input("Frozen shrimp boxes currently in stock:", min_value=0, value=0)
shrimp_order = max(0, 5 - shrimp)

if st.button("Calculate Order"):
    st.success("✅ Order Summary:")
    st.write(f"- Tofu boxes to order: **{tofu_order}**")
    st.write(f"- Chicken boxes to order: **{chicken_order}**")
    st.write(f"- Liquid egg boxes to order: **{egg_order}**")
    st.write(f"- Scallion pancake boxes to order: **{pancake_order}**")
    st.write(f"- Lo mein boxes to order: **{lo_mein_order}**")
    st.write(f"- Cooking wine boxes to order: **{cooking_wine_order}**")
    st.write(f"- Edamame pod boxes to order: **{edamame_order}**")
    st.write(f"- Degreaser boxes to order: **{degreaser_order}**")
    st.write(f"- Frozen shrimp boxes to order: **{shrimp_order}**")

    st.info("You can copy this summary and send it with your order.")
