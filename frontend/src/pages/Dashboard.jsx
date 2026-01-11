import { useState, useEffect } from 'react';
import { CreditCard, TrendingUp, Calendar, AlertCircle } from 'lucide-react';
import '../index.css';

const StatCard = ({ title, value, icon: Icon, color }) => (
    <div className="glass-panel p-6 flex flex-col items-start hover:bg-[rgba(255,255,255,0.05)] transition-colors">
        <div className="flex items-center justify-between w-full mb-4">
            <span className="text-secondary text-sm font-medium">{title}</span>
            <div className={`p-2 rounded-lg bg-[${color}]/20 text-[${color}]`}>
                <Icon size={20} style={{ color: color }} />
            </div>
        </div>
        <span className="text-3xl font-bold">{value}</span>
    </div>
);

const Dashboard = () => {
    const [stats, setStats] = useState({
        monthlySpend: 24500.00,
        upcomingPayment: 5400.00,
        dueDate: '15/01/2026'
    });

    return (
        <div className="container mx-auto px-4 py-8">
            <header className="mb-10">
                <h1 className="text-4xl font-bold mb-2">Welcome Back</h1>
                <p className="text-secondary text-lg">Here's your credit card summary for January</p>
            </header>

            {/* Stats Grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
                <StatCard
                    title="Total Spent (Month)"
                    value={`RD$ ${stats.monthlySpend.toLocaleString()}`}
                    icon={TrendingUp}
                    color="#a855f7"
                />
                <StatCard
                    title="Upcoming Payment"
                    value={`RD$ ${stats.upcomingPayment.toLocaleString()}`}
                    icon={CreditCard}
                    color="#6366f1"
                />
                <StatCard
                    title="Days until Due Date"
                    value="4 Days"
                    icon={Calendar}
                    color="#ec4899"
                />
            </div>

            {/* Recent Transactions Preview */}
            <div className="glass-panel p-8">
                <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
                    <AlertCircle size={20} className="text-accent-secondary" />
                    Recent Activity
                </h2>

                <div className="overflow-x-auto">
                    <table className="w-full text-left">
                        <thead className="text-secondary text-sm border-b border-glass-border">
                            <tr>
                                <th className="pb-4 font-medium">Merchant</th>
                                <th className="pb-4 font-medium">Date</th>
                                <th className="pb-4 font-medium">Amount</th>
                                <th className="pb-4 font-medium">Status</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-glass-border">
                            <tr className="group hover:bg-glass-bg transition-colors">
                                <td className="py-4">Uber Eats</td>
                                <td className="py-4 text-sm text-secondary">Jan 10, 2026</td>
                                <td className="py-4 font-medium">RD$ 450.00</td>
                                <td className="py-4"><span className="px-2 py-1 rounded-full text-xs font-semibold bg-blue-500/20 text-blue-300">Unpaid</span></td>
                            </tr>
                            <tr className="group hover:bg-glass-bg transition-colors">
                                <td className="py-4">Netflix Subscription</td>
                                <td className="py-4 text-sm text-secondary">Jan 08, 2026</td>
                                <td className="py-4 font-medium">US$ 15.99</td>
                                <td className="py-4"><span className="px-2 py-1 rounded-full text-xs font-semibold bg-green-500/20 text-green-300">Paid</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
