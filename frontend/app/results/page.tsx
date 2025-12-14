"use client";

import React, { useEffect, useState, Suspense } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';
import { Button } from "@/components/ui/button";
import ScoreCard from '@/components/ScoreCard';
import RoadmapList from '@/components/RoadmapList';
import { Loader2, ArrowLeft } from 'lucide-react';

interface AnalysisData {
    repo_name: string;
    owner: string;
    score: number;
    breakdown: any;
    summary: string;
    roadmap: string[];
}

function ResultsContent() {
    const searchParams = useSearchParams();
    const router = useRouter();
    const repoUrl = searchParams.get('repo');

    const [data, setData] = useState<AnalysisData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        if (!repoUrl) {
            router.push('/');
            return;
        }

        const fetchData = async () => {
            try {
                // In production, use env var
                const res = await fetch('http://localhost:8000/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: repoUrl })
                });

                if (!res.ok) {
                    const err = await res.json();
                    throw new Error(err.detail || 'Failed to analyze repository');
                }

                const json = await res.json();
                setData(json);
            } catch (err: any) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [repoUrl, router]);

    if (loading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen space-y-4">
                <div className="relative">
                    <div className="absolute inset-0 bg-blue-500 blur-xl opacity-20 rounded-full"></div>
                    <Loader2 className="h-16 w-16 animate-spin text-primary relative z-10" />
                </div>
                <h2 className="text-xl font-medium animate-pulse">Analyzing Repository...</h2>
                <p className="text-muted-foreground">Fetching metadata, scanning code, and generating insights.</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen space-y-6">
                <div className="text-red-500 font-bold text-2xl">Analysis Failed</div>
                <p className="text-muted-foreground">{error}</p>
                <Button onClick={() => router.push('/')} variant="outline">
                    <ArrowLeft className="mr-2 h-4 w-4" /> Try Another Repo
                </Button>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-background p-8 flex flex-col items-center">
            <div className="w-full max-w-4xl mb-8 flex items-center justify-between">
                <Button variant="ghost" onClick={() => router.push('/')} className="hover:bg-primary/10">
                    <ArrowLeft className="mr-2 h-4 w-4" /> Back
                </Button>
                <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">
                    {data?.owner}/{data?.repo_name}
                </h1>
            </div>

            {data && (
                <div className="w-full flex flex-col items-center space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-700">
                    <ScoreCard score={data.score} breakdown={data.breakdown} summary={data.summary} />
                    <RoadmapList steps={data.roadmap} />
                </div>
            )}
        </div>
    );
}

export default function Results() {
    return (
        <Suspense fallback={<div className="flex items-center justify-center min-h-screen"><Loader2 className="animate-spin" /></div>}>
            <ResultsContent />
        </Suspense>
    );
}
