import streamlit as st

st.set_page_config(page_title="Advanced Salary & Loan Calculator", layout="centered")
class Loan:
    def __init__(self, amount, interest_rate, months):
        self.amount = amount
        self.interest_rate = interest_rate
        self.months = months

    def monthly_payment(self):
        if self.months == 0:
            return 0
        monthly_interest = (self.interest_rate / 100) * self.amount / self.months
        return (self.amount / self.months) + monthly_interest

st.title("💰 Advanced Salary & Loan Calculator")

salary = st.number_input("Enter Gross Monthly Salary (UGX)", min_value=0, step=10000)


tax_rate = st.slider("Tax Rate (%)", 0, 50, 10)
tax = (tax_rate / 100) * salary



with st.expander("📉 Add Loan Deduction"):
    has_loan = st.checkbox("Include Loan Deduction?")
    if has_loan:
        loan_amount = st.number_input("Loan Amount (UGX)", min_value=0)
        interest_rate = st.slider("Loan Interest Rate (%)", 0, 30, 10)
        months = st.slider("Repayment Period (months)", 1, 60, 12)

        
        loan = Loan(loan_amount, interest_rate, months)
        monthly_loan_payment = loan.monthly_payment()
    else:
        monthly_loan_payment = 0


total_deductions = tax + monthly_loan_payment
net_salary = salary - total_deductions


st.markdown("---")
st.subheader(" Summary")
st.write(f"**Gross Salary:** UGX {salary:,.0f}")
st.write(f"**Tax:** UGX {tax:,.0f}")
if has_loan:
    st.write(f"**Loan Deduction:** UGX {monthly_loan_payment:,.0f}")
st.markdown(f"###  Net Salary: UGX {net_salary:,.0f}")


