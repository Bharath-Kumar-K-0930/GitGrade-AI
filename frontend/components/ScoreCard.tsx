"use client";
import React from "react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Trophy, Award, Medal } from "lucide-react";
import { Progress } from "@/components/ui/progress";

interface ScoreCardProps {
    score: number;
}

const ScoreCard: React.FC<ScoreCardProps> = ({ score }) => {
    const getLevel = (s: number) => {
        if (s >= 71) return { label: "Advanced", color: "text-purple-400", badge: "Gold Developer", icon: Trophy, badgeColor: "bg-yellow-500" };
        if (s >= 41) return { label: "Intermediate", color: "text-blue-400", badge: "Silver Developer", icon: Medal, badgeColor: "bg-gray-400" };
        return { label: "Beginner", color: "text-yellow-400", badge: "Bronze Developer", icon: Award, badgeColor: "bg-orange-600" };
    };

    const level = getLevel(score);
    const Icon = level.icon;

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
                    <span className={`px-4 py-1.5 rounded-full text-sm font-bold text-white shadow-lg ${level.badgeColor}`}>
                        {level.badge}
                    </span>
                </div>
            </CardHeader>

            <CardContent className="space-y-6">
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
            </CardContent>
        </Card>
    );
};

export default ScoreCard;
