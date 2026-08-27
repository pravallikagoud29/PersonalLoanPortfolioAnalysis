import {
  GraduationCap,
  DollarSign,
  PiggyBank,
  CreditCard,
  Users,
  Wifi,
  TrendingUp,
  Calendar,
  type LucideIcon,
} from "lucide-react";

const iconMap: Record<string, LucideIcon> = {
  GraduationCap,
  DollarSign,
  PiggyBank,
  CreditCard,
  Users,
  Wifi,
  TrendingUp,
  Calendar,
};

/* ---------- Hero ---------- */
export function Hero() {
  return (
    <header className="relative overflow-hidden bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 pb-24 pt-16">
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-10 left-10 w-72 h-72 bg-blue-400 rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-10 w-96 h-96 bg-emerald-400 rounded-full blur-3xl" />
      </div>
      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="inline-flex items-center gap-2 bg-blue-500/20 text-blue-300 text-sm font-medium px-4 py-1.5 rounded-full mb-6">
          <TrendingUp className="w-4 h-4" />
          Exploratory Data Analysis
        </div>
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white tracking-tight">
          Personal Loan Portfolio Analysis
        </h1>
        <p className="mt-4 text-lg sm:text-xl text-slate-300 max-w-2xl">
          Apex Credit Union — understanding the demographics and loan
          characteristics of personal loan customers through data-driven
          exploratory analysis.
        </p>
        <div className="mt-8 flex flex-wrap gap-6 text-slate-300">
          <div className="flex items-center gap-2">
            <Users className="w-5 h-5 text-blue-400" />
            <span>500 customers</span>
          </div>
          <div className="flex items-center gap-2">
            <DollarSign className="w-5 h-5 text-emerald-400" />
            <span>14 attributes</span>
          </div>
          <div className="flex items-center gap-2">
            <TrendingUp className="w-5 h-5 text-amber-400" />
            <span>19.4% acceptance rate</span>
          </div>
        </div>
      </div>
    </header>
  );
}

/* ---------- Stat Card ---------- */
export function StatCard({
  icon,
  label,
  value,
  color,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  color: string;
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 hover:shadow-md transition-shadow">
      <div
        className={`inline-flex items-center justify-center w-12 h-12 rounded-lg text-white mb-3 ${color}`}
      >
        {icon}
      </div>
      <p className="text-2xl font-bold text-slate-900">{value}</p>
      <p className="text-sm text-slate-500 mt-0.5">{label}</p>
    </div>
  );
}

/* ---------- Section Header ---------- */
export function SectionHeader({
  title,
  subtitle,
}: {
  title: string;
  subtitle: string;
}) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-slate-900">{title}</h2>
      <p className="text-slate-500 mt-1">{subtitle}</p>
    </div>
  );
}

/* ---------- Bar Chart Card ---------- */
type BarDatum = { label: string; rate: number; count: number };

export function BarChartCard({
  title,
  subtitle,
  data,
  color,
}: {
  title: string;
  subtitle: string;
  data: BarDatum[];
  color: string;
}) {
  const maxRate = Math.max(...data.map((d) => d.rate));

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <h3 className="text-lg font-semibold text-slate-900">{title}</h3>
      <p className="text-sm text-slate-500 mb-5">{subtitle}</p>
      <div className="space-y-4">
        {data.map((d) => (
          <div key={d.label}>
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-sm font-medium text-slate-700">
                {d.label}
              </span>
              <span className="text-sm font-bold text-slate-900">
                {d.rate}%
              </span>
            </div>
            <div className="relative h-7 bg-slate-100 rounded-lg overflow-hidden">
              <div
                className="absolute inset-y-0 left-0 rounded-lg flex items-center justify-end pr-2 transition-all duration-700 ease-out"
                style={{
                  width: `${(d.rate / maxRate) * 100}%`,
                  backgroundColor: color,
                }}
              >
                <span className="text-xs text-white font-medium">
                  {d.count} customers
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ---------- Product Comparison Card ---------- */
export function ProductComparisonCard({
  product,
}: {
  product: {
    label: string;
    yesRate: number;
    noRate: number;
    yesCount: number;
    noCount: number;
  };
}) {
  const diff = (product.yesRate - product.noRate).toFixed(1);
  const isPositive = product.yesRate >= product.noRate;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
      <h3 className="text-base font-semibold text-slate-900 mb-4">
        {product.label}
      </h3>
      <div className="space-y-3">
        <div>
          <div className="flex justify-between text-sm mb-1">
            <span className="text-slate-600">Has product</span>
            <span className="font-bold text-emerald-600">{product.yesRate}%</span>
          </div>
          <div className="h-4 bg-slate-100 rounded overflow-hidden">
            <div
              className="h-full bg-emerald-500 rounded transition-all duration-700"
              style={{ width: `${product.yesRate * 2}%` }}
            />
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            {product.yesCount} customers
          </p>
        </div>
        <div>
          <div className="flex justify-between text-sm mb-1">
            <span className="text-slate-600">No product</span>
            <span className="font-bold text-slate-500">{product.noRate}%</span>
          </div>
          <div className="h-4 bg-slate-100 rounded overflow-hidden">
            <div
              className="h-full bg-slate-400 rounded transition-all duration-700"
              style={{ width: `${product.noRate * 2}%` }}
            />
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            {product.noCount} customers
          </p>
        </div>
      </div>
      <div
        className={`mt-4 text-xs font-medium px-2.5 py-1 rounded-full inline-block ${
          isPositive
            ? "bg-emerald-50 text-emerald-700"
            : "bg-slate-100 text-slate-500"
        }`}
      >
        {isPositive ? "+" : ""}
        {diff} pts difference
      </div>
    </div>
  );
}

/* ---------- Correlation Card ---------- */
export function CorrelationCard({
  correlations,
}: {
  correlations: { feature: string; value: number }[];
}) {
  const maxAbs = Math.max(...correlations.map((c) => Math.abs(c.value)));

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="space-y-2.5">
        {correlations.map((c) => {
          const isPositive = c.value >= 0;
          const widthPct = (Math.abs(c.value) / maxAbs) * 100;
          return (
            <div key={c.feature} className="flex items-center gap-3">
              <span className="text-sm font-medium text-slate-700 w-36 shrink-0">
                {c.feature}
              </span>
              <div className="flex-1 relative h-6 bg-slate-50 rounded">
                <div className="absolute left-1/2 top-0 bottom-0 w-px bg-slate-300" />
                <div
                  className={`absolute top-0 bottom-0 rounded transition-all duration-700 ${
                    isPositive ? "bg-blue-500" : "bg-rose-400"
                  }`}
                  style={{
                    left: isPositive ? "50%" : `${50 - widthPct}%`,
                    width: `${widthPct / 2}%`,
                  }}
                />
              </div>
              <span
                className={`text-sm font-bold w-12 text-right ${
                  isPositive ? "text-blue-600" : "text-rose-500"
                }`}
              >
                {c.value > 0 ? "+" : ""}
                {c.value}
              </span>
            </div>
          );
        })}
      </div>
      <p className="text-xs text-slate-400 mt-4">
        Values closer to +1 or -1 indicate a stronger relationship. Income and
        CCAvg show the strongest positive correlation with loan acceptance.
      </p>
    </div>
  );
}

/* ---------- Insight Card ---------- */
export function InsightCard({
  insight,
}: {
  insight: { title: string; text: string; icon: string };
}) {
  const Icon = iconMap[insight.icon] ?? TrendingUp;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 hover:shadow-md transition-shadow">
      <div className="flex gap-4">
        <div className="shrink-0 w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center">
          <Icon className="w-5 h-5 text-blue-600" />
        </div>
        <div>
          <h3 className="font-semibold text-slate-900 text-sm">
            {insight.title}
          </h3>
          <p className="text-sm text-slate-600 mt-1 leading-relaxed">
            {insight.text}
          </p>
        </div>
      </div>
    </div>
  );
}

/* ---------- Executive Summary ---------- */
export function ExecutiveSummary({
  summary,
}: {
  summary: {
    findings: string[];
    segments: { name: string; reason: string }[];
    recommendations: string[];
  };
}) {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Key Findings */}
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-blue-600" />
          Key Findings
        </h3>
        <ul className="space-y-3">
          {summary.findings.map((f, i) => (
            <li key={i} className="flex gap-2.5 text-sm text-slate-600">
              <span className="shrink-0 w-5 h-5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold flex items-center justify-center mt-0.5">
                {i + 1}
              </span>
              <span className="leading-relaxed">{f}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Important Segments */}
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
          <Users className="w-5 h-5 text-emerald-600" />
          Important Segments
        </h3>
        <div className="space-y-3">
          {summary.segments.map((s, i) => (
            <div
              key={i}
              className="border-l-2 border-emerald-500 pl-3 py-1"
            >
              <p className="text-sm font-semibold text-slate-900">
                {s.name}
              </p>
              <p className="text-xs text-slate-500 mt-0.5">{s.reason}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Recommendations */}
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <h3 className="font-bold text-slate-900 mb-4 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-amber-600" />
          Recommendations
        </h3>
        <ul className="space-y-3">
          {summary.recommendations.map((r, i) => (
            <li key={i} className="flex gap-2.5 text-sm text-slate-600">
              <span className="shrink-0 text-amber-500 font-bold mt-0.5">
                {i + 1}.
              </span>
              <span className="leading-relaxed">{r}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
