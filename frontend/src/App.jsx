import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { LayoutDashboard, CreditCard, Settings, Wallet } from 'lucide-react';
import Dashboard from './pages/Dashboard';
import './index.css';

const Navigation = () => (
  <nav className="fixed left-0 top-0 h-full w-64 glass-panel border-r border-glass-border m-4 rounded-2xl flex flex-col p-6 z-10 hidden md:flex">
    <div className="flex items-center gap-3 mb-12">
      <div className="p-2 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg">
        <Wallet size={24} color="white" />
      </div>
      <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">
        TC Helper
      </span>
    </div>

    <div className="flex flex-col gap-2">
      <NavLink to="/" icon={LayoutDashboard} label="Dashboard" active />
      <NavLink to="/transactions" icon={CreditCard} label="Transactions" />
      <NavLink to="/settings" icon={Settings} label="Settings" />
    </div>

    <div className="mt-auto">
      <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-900/50 to-purple-900/50 border border-indigo-500/20">
        <p className="text-xs text-indigo-300 font-semibold mb-1">PRO PLAN</p>
        <p className="text-sm text-gray-300">Sync is active</p>
      </div>
    </div>
  </nav>
);

const NavLink = ({ to, icon: Icon, label, active }) => (
  <Link
    to={to}
    className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-300 group
      ${active ? 'bg-white/10 text-white shadow-lg shadow-indigo-500/10' : 'text-gray-400 hover:bg-white/5 hover:text-white'}
    `}
  >
    <Icon size={20} className={active ? 'text-indigo-400' : 'group-hover:text-indigo-400 transition-colors'} />
    <span className="font-medium">{label}</span>
  </Link>
);

function App() {
  return (
    <Router>
      <div className="min-h-screen pl-0 md:pl-72 transition-all duration-300">
        <Navigation />
        <main className="min-h-screen">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/transactions" element={<div className="p-10 text-center text-gray-400">Transactions View Coming Soon</div>} />
            <Route path="/settings" element={<div className="p-10 text-center text-gray-400">Settings Coming Soon</div>} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
