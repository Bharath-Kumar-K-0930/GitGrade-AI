"use client";
import React from 'react';
import RepoInput from "@/components/RepoInput";
import { GitBranch } from "lucide-react";

export default function Home() {
    return (
        <main className="min-h-screen flex flex-col items-center justify-center p-6 bg-black text-white relative overflow-hidden">
            {/* Background Ambience */}
            <div className="absolute top-[-20%] left-[-20%] w-[60%] h-[60%] bg-purple-900/20 rounded-full blur-[120px]" />
            <div className="absolute bottom-[-20%] right-[-20%] w-[60%] h-[60%] bg-blue-900/20 rounded-full blur-[120px]" />

            <div className="z-10 w-full max-w-xl space-y-8 animate-fade-in text-center">
                <div className="flex justify-center mb-6">
                    <div className="p-4 rounded-2xl bg-gray-900 border border-gray-800 shadow-2xl">
                        <GitBranch className="h-16 w-16 text-blue-500" />
                    </div>
                </div>

                <h1 className="text-5xl md:text-6xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-br from-white to-gray-400">
                    GitGrade AI
                </h1>

                <p className="text-lg text-gray-400 leading-relaxed font-light">
                    Your GitHub. Evaluated like a Recruiter.<br />
                    <span className="text-sm opacity-70">Turn repositories into scores, insights, and growth roadmaps.</span>
                </p>

                <RepoInput />

                <div className="pt-8 flex justify-center gap-8 text-xs font-mono text-gray-600">
                    <span>STATIC ANALYSIS</span>
                    <span>•</span>
                    <span>AI MENTORSHIP</span>
                    <span>•</span>
                    <span>RECRUITER STANDARD</span>
                </div>
            </div>
        </main>
    );
}
