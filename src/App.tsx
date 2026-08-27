import { BarChart3, TrendingUp, Users, DollarSign } from "lucide-react";
import {
  metrics,
  byEducation,
  byIncome,
  byAge,
  byFamily,
  byProduct,
  correlations,
  insights,
  executiveSummary,
} from "@/data/loanData";
import {
  StatCard,
  BarChartCard,
  ProductComparisonCard,
  CorrelationCard,
  InsightCard,
  ExecutiveSummary,
  SectionHeader,
  Hero,
} from "@/components/Dashboard";

export default function App() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-800">
      {/* Hero */}
      <Hero />

      {/* Key Metrics */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-16 relative z-10">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <StatCard
            icon={<Users className="w-6 h-6" />}
            label="Total Customers"
            value={metrics.total.toLocaleString()}
            color="bg-blue-600"
          />
          <StatCard
            icon={<DollarSign className="w-6 h-6" />}
            label="Average Income"
            value={`$${metrics.avgIncome}K`}
            color="bg-emerald-600"
          />
          <StatCard
            icon={<TrendingUp className="w-6 h-6" />}
            label="Loan Acceptance Rate"
            value={`${metrics.loanRate}%`}
            color="bg-amber-500"
          />
          <StatCard
            icon={<BarChart3 className="w-6 h-6" />}
            label="Average Age"
            value={`${metrics.avgAge} yrs`}
            color="bg-rose-500"
          />
        </div>
      </section>

      {/* Demographics */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
        <SectionHeader
          title="Customer Demographics"
          subtitle="Who are Apex Credit Union's personal loan customers?"
        />
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
          <BarChartCard
            title="Loan Acceptance by Income Group"
            subtitle="Data-driven tertiles (low / medium / high)"
            data={byIncome}
            color="#2563eb"
          />
          <BarChartCard
            title="Loan Acceptance by Education Level"
            subtitle="Undergraduate vs Graduate vs Advanced"
            data={byEducation}
            color="#059669"
          />
          <BarChartCard
            title="Loan Acceptance by Age Group"
            subtitle="Five age brackets from under 30 to over 60"
            data={byAge}
            color="#d97706"
          />
          <BarChartCard
            title="Loan Acceptance by Family Size"
            subtitle="Single to large families (1-4 members)"
            data={byFamily}
            color="#e11d48"
          />
        </div>
      </section>

      {/* Banking Products */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
        <SectionHeader
          title="Existing Banking Products"
          subtitle="How do existing products relate to loan acceptance?"
        />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          {byProduct.map((p) => (
            <ProductComparisonCard key={p.label} product={p} />
          ))}
        </div>
      </section>

      {/* Correlation */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
        <SectionHeader
          title="Correlation Analysis"
          subtitle="Which numeric features correlate most with Personal Loan acceptance?"
        />
        <div className="mt-6">
          <CorrelationCard correlations={correlations} />
        </div>
      </section>

      {/* Insights */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12">
        <SectionHeader
          title="Business Insights"
          subtitle="Eight data-backed insights for Apex Credit Union"
        />
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          {insights.map((insight, i) => (
            <InsightCard key={i} insight={insight} />
          ))}
        </div>
      </section>

      {/* Executive Summary */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 mb-16">
        <SectionHeader
          title="Executive Summary"
          subtitle="Key findings, important segments, and recommendations"
        />
        <div className="mt-6">
          <ExecutiveSummary summary={executiveSummary} />
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-slate-400 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-sm">
            Personal Loan Portfolio Analysis — Apex Credit Union
          </p>
          <p className="text-xs mt-1 text-slate-500">
            Exploratory Data Analysis with Python, Pandas, Matplotlib & Seaborn
          </p>
        </div>
      </footer>
    </div>
  );
}
