"use client";

import React, { useEffect, useState, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { Loader2, ArrowLeft, Download } from "lucide-react";
import { Button } from "@/components/ui/button";
import ScoreCard from "@/components/ScoreCard";
import SummaryCard from "@/components/SummaryCard";
import RoadmapList from "@/components/RoadmapList";

interface AnalysisData {
    repo_name: string;
    owner: string;
    score: number;
    level: string;
    summary: string;
    roadmap: string[];
    breakdown?: Record<string, number>;
    verdict?: string;
}

function ResultPageContent() {
    const repoUrl = useSearchParams().get("repo");
    const [data, setData] = useState<AnalysisData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const router = useRouter();

    useEffect(() => {
        // Use relative URL for Vercel (production), but full URL for localhost dev
        // If window.location.hostname is localhost, assume backend is at :8000
        const isLocal = typeof window !== 'undefined' && window.location.hostname === 'localhost';
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || (isLocal ? "http://localhost:8000/analyze" : "/api/analyze");

        if (!repoUrl) return;

        fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: repoUrl }),
        })
            .then(async (res) => {
                if (!res.ok) {
                    const errText = await res.text();
                    throw new Error(`Server Error: ${res.status} ${errText}`);
                }
                return res.json();
            })
            .then((data) => {
                setData(data);
            })
            .catch((err) => {
                console.error("Fetch error:", err);
                setError(err.message || "Failed to connect to GitGrade AI Service.");
            })
            .finally(() => {
                setLoading(false);
            });
    }, [repoUrl]);

    const handleDownloadPdf = () => {
        if (!data) return;
        const roadmapStr = data.roadmap.join(',');

        // Consistent URL logic
        const isLocal = typeof window !== 'undefined' && window.location.hostname === 'localhost';
        let baseUrl = process.env.NEXT_PUBLIC_API_URL || (isLocal ? "http://localhost:8000" : "/api");

        // Remove trailing slash or /analyze if present
        baseUrl = baseUrl.replace(/\/analyze$/, '').replace(/\/$/, '');

        const url = `${baseUrl}/download-pdf?repo=${data.repo_name}&score=${data.score}&summary=${encodeURIComponent(data.summary)}&roadmap=${encodeURIComponent(roadmapStr)}`;
        window.open(url, '_blank');
    };

    if (!repoUrl) return <div className="text-white text-center mt-20">No repository provided.</div>;

    if (loading) {
        return (
            <div className="min-h-screen bg-black flex flex-col items-center justify-center space-y-6 text-white">
                <div className="relative">
                    <div className="absolute inset-0 bg-blue-600 blur-2xl opacity-20 rounded-full" />
                    <Loader2 className="h-16 w-16 animate-spin text-blue-500 relative z-10" />
                </div>
                <p className="text-xl animate-pulse font-light tracking-wide">Analyzing Code & Commits...</p>
                <p className="text-sm text-gray-500">Connecting to GitHub API • Scanning Structure • Generating Roadmap</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="min-h-screen bg-black flex flex-col items-center justify-center text-white space-y-4">
                <p className="text-red-500 text-xl font-bold">Error: {error}</p>
                <Button variant="secondary" onClick={() => router.push('/')}>Try Again</Button>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-black text-white p-6 md:p-12 font-sans">
            <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-10 duration-1000">

                {/* Header */}
                <div className="flex items-center justify-between">
                    <Button variant="ghost" className="text-gray-400 hover:text-white" onClick={() => router.push('/')}>
                        <ArrowLeft className="mr-2 h-4 w-4" /> Back
                    </Button>
                    <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">
                        {data?.owner} / {data?.repo_name}
                    </h1>
                    <Button variant="outline" className="border-gray-700 text-gray-300 hover:bg-gray-800" onClick={handleDownloadPdf}>
                        <Download className="mr-2 h-4 w-4" /> Report
                    </Button>
                </div>

                {/* Content */}
                {data && (
                    <>
                        <ScoreCard score={data.score} verdict={data.verdict} />
                        <SummaryCard summary={data.summary} />
                        <RoadmapList roadmap={data.roadmap} />
                    </>
                )}
            </div>
        </div>
    );
}

export default function ResultPage() {
    return (
        <Suspense fallback={<div className="min-h-screen bg-black text-white flex items-center justify-center">Loading...</div>}>
            <ResultPageContent />
        </Suspense>
    );
}
