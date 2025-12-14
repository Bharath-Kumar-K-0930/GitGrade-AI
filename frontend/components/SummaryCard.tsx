import React from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { FileText } from "lucide-react";

interface SummaryCardProps {
    summary: string;
}

const SummaryCard: React.FC<SummaryCardProps> = ({ summary }) => {
    return (
        <Card className="w-full max-w-4xl bg-gray-900/50 border-gray-700 text-white">
            <CardHeader>
                <CardTitle className="flex items-center gap-2 text-xl text-blue-400">
                    <FileText className="h-5 w-5" />
                    AI Recruiter Summary
                </CardTitle>
            </CardHeader>
            <CardContent>
                <p className="text-lg leading-relaxed text-gray-300">
                    {summary}
                </p>
            </CardContent>
        </Card>
    );
};

export default SummaryCard;
