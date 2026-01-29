import { createContext, useContext, useState } from 'react';

const LoanContext = createContext(null);

export const useLoan = () => {
    const context = useContext(LoanContext);
    if (!context) {
        throw new Error("useLoan must be used within a LoanProvider");
    }
    return context;
};

export const LoanProvider = ({ children }) => {
    const [currentLoan, setCurrentLoan] = useState(null);
    const [loans, setLoans] = useState([]);

    const applyForLoan = async (loanData) => {
        // Mock API call
        return new Promise((resolve) => {
            setTimeout(() => {
                console.log('Submitting loan application:', loanData);
                const newLoan = {
                    id: Date.now(),
                    ...loanData,
                    status: 'Pending',
                    appliedDate: new Date().toISOString()
                };
                setLoans((prev) => [...prev, newLoan]);
                setCurrentLoan(newLoan);
                resolve(newLoan);
            }, 1500);
        });
    };

    return (
        <LoanContext.Provider value={{ currentLoan, loans, applyForLoan }}>
            {children}
        </LoanContext.Provider>
    );
};
