"use client";
import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Trophy, Award, Medal } from "lucide-react";
import { Progress } from "@/components/ui/progress";

interface ScoreCardProps {
    score: number;
    breakdown?: Record<string, number>;
    summary?: string;
    verdict?: string;
}

const ScoreCard: React.FC<ScoreCardProps> = ({ score, breakdown, summary, verdict }) => {
    const getLevel = (s: number) => {
        if (s >= 71) return { label: "Advanced", color: "text-purple-400", badge: "Gold Developer", icon: Trophy, badgeColor: "bg-yellow-500" };
        if (s >= 41) return { label: "Intermediate", color: "text-blue-400", badge: "Silver Developer", icon: Medal, badgeColor: "bg-gray-400" };
        return { label: "Beginner", color: "text-yellow-400", badge: "Bronze Developer", icon: Award, badgeColor: "bg-orange-600" };
    };

    const level = getLevel(score);
    const Icon = level.icon;

    // Helper to get max score for category
    const getMax = (cat: string) => {
        if (cat.includes("Code Quality")) return 25;
        if (cat.includes("Product") || cat.includes("Structure") || cat.includes("Git")) return 15;
        return 10;
    };

    return (
        <Card className="w-full max-w-4xl bg-gray-900/50 border-gray-700 text-white relative overflow-hidden">
            <div className="absolute top-0 right-0 p-4 opacity-10">
                <Icon className="h-40 w-40" />
            </div>

            <CardHeader>
                <div className="flex justify-between items-start">
                    <div>
                        <CardTitle className="text-2xl font-bold">GitGrade Score</CardTitle>
                        <CardDescription className="text-gray-400">Based on recruiter-standard metrics</CardDescription>
                    </div>
                    <div className="flex flex-col items-end gap-2">
                        <span className={`px-4 py-1.5 rounded-full text-sm font-bold text-white shadow-lg ${level.badgeColor}`}>
                            {level.badge}
                        </span>
                        {verdict && (
                            <span className="text-xs font-mono uppercase tracking-widest text-emerald-400 border border-emerald-900/50 px-2 py-1 rounded bg-emerald-900/20">
                                {verdict}
                            </span>
                        )}
                    </div>
                </div>
            </CardHeader>

            <CardContent className="space-y-8">
                {/* Main Score & Progress */}
                <div className="space-y-6">
                    <div className="flex items-end gap-2">
                        <span className={`text-6xl font-black ${level.color} transition-all duration-700`}>
                            {score}
                        </span>
                        <span className="text-xl text-gray-500 mb-2">/ 100</span>
                        <span className={`text-2xl font-semibold mb-2 ml-2 ${level.color}`}>
                            ({level.label})
                        </span>
                    </div>

                    <div className="space-y-2">
                        <Progress value={score} className="h-4 bg-gray-800" indicatorClassName={score > 70 ? "bg-purple-500" : score > 40 ? "bg-blue-500" : "bg-yellow-500"} />
                        <div className="flex justify-between text-xs text-gray-500 font-mono">
                            <span>Beginner (0-40)</span>
                            <span>Intermediate (41-70)</span>
                            <span>Advanced (71-100)</span>
                        </div>
                    </div>
                </div>

                {/* Professor's Breakdown Table */}
                {breakdown && (
                    <div className="bg-gray-800/50 rounded-lg p-4 border border-gray-700">
                        <h3 className="text-lg font-semibold mb-4 text-gray-200 border-b border-gray-700 pb-2 flex justify-between">
                            <span>🧠 Recruiter's Signal Breakdown</span>
                            <span className="text-xs text-gray-500 font-normal self-end">Target: 100 pts</span>
                        </h3>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4">
                            {Object.entries(breakdown).map(([category, marks]) => {
                                const max = getMax(category);
                                const percentage = marks / max;
                                const color = percentage > 0.8 ? "text-green-400" : percentage > 0.5 ? "text-yellow-400" : "text-red-400";

                                return (
                                    <div key={category} className="flex justify-between items-center border-b border-gray-800 pb-1">
                                        <span className="text-sm text-gray-300 truncate pr-2" title={category}>{category}</span>
                                        <span className={`font-mono font-bold ${color}`}>
                                            {marks} <span className="text-gray-600 text-xs text-opacity-50">/ {max}</span>
                                        </span>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                )}

                {/* Summary Section (Moved inside card for cohesion) */}
                {summary && (
                    <div className="bg-blue-900/20 border border-blue-800 rounded-lg p-4">
                        <h4 className="text-blue-400 font-semibold mb-1 flex items-center">
                            <span className="mr-2">📝</span> AI Local Summary
                        </h4>
                        <p className="text-gray-300 text-sm leading-relaxed">
                            {summary}
                        </p>
                    </div>
                )}
            </CardContent>
        </Card>
    );
};

export default ScoreCard;
