import streamlit as st
from content_generation_crew import ContentGenerationCrew
import time
from datetime import datetime
import markdown

st.set_page_config(
    page_title="AI Content Generation Pipeline",
    page_icon="✍️",
    layout="wide"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .sub-text {
        color: #64748b;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .agent-card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 16px;
        margin-bottom: 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    
    .agent-card:hover {
        transform: translateY(-4px);
        border-color: #3b82f6;
    }
    
    .task-status {
        padding: 0.75rem 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .pending { background-color: #f1f5f9; color: #64748b; border: 1px solid #e2e8f0; }
    .in-progress { background-color: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
    .completed { background-color: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
    
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
        font-size: 1.1rem;
        box-shadow: 0 4px 14px 0 rgba(0, 118, 255, 0.39);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 118, 255, 0.23);
    }
</style>
""", unsafe_allow_html=True)

# Initialize crew
@st.cache_resource
def get_crew():
    return ContentGenerationCrew()

# Header
st.markdown('<p class="main-header">✍️ AI Content Pipeline</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Collaborative multi-agent system powered by CrewAI & DeepSeek</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("🤖 AI Agent Team")
    agents_info = {
        "Researcher": ("🔍", "Information specialist"),
        "Writer": ("✍️", "Narrative expert"),
        "Editor": ("📝", "Refinement master"),
        "Fact Checker": ("✅", "Accuracy scout"),
        "SEO Guru": ("📈", "Search optimizer")
    }
    
    for agent, (icon, role) in agents_info.items():
        st.markdown(f"""
        <div class="agent-card">
            <strong>{icon} {agent}</strong><br>
            <span style="font-size: 0.85rem; color: #64748b;">{role}</span>
        </div>
        """, unsafe_allow_html=True)

# Main UI
topic = st.text_input("What is the topic of your content?", placeholder="e.g., The Future of Sustainable Energy")

content_type = st.selectbox("Select Content Type", 
                          ["Blog Post", "Research Report", "Technical Article", "Newsletter"])

if st.button("🚀 Generate High-Quality Content"):
    if not topic:
        st.error("Please enter a topic.")
    else:
        try:
            crew = get_crew()
            
            with st.status("🎬 Crew is starting the process...", expanded=True) as status:
                st.write("🔍 Researcher is gathering data...")
                # In a real app, you'd hook into CrewAI's verbose output or callbacks
                # For now, we'll simulate steps or just call kickoff
                
                start_time = time.time()
                result = crew.generate_content(topic, content_type)
                end_time = time.time()
                
                status.update(label="✅ Content Generation Complete!", state="complete", expanded=False)
            
            # Results Display
            st.success(f"Generated successfully in {end_time - start_time:.1f} seconds!")
            
            # Score the content
            from quality_scorer import ContentQualityScorer
            scorer = ContentQualityScorer()
            quality_results = scorer.score_content(result["final_content"], topic)
            
            # Save Version
            from content_versioning import ContentVersionControl
            vc = ContentVersionControl()
            version_id = vc.save_version(topic, result["final_content"])
            
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["📄 Content View", "🛠️ Raw Markdown", "📊 Stats", "⭐ Quality Score", "📜 History"])
            
            with tab1:
                st.markdown(result["final_content"])
                
            with tab2:
                st.code(result["final_content"], language="markdown")
                
            with tab3:
                cols = st.columns(3)
                cols[0].metric("Agents Involved", result["agents_used"])
                cols[1].metric("Tasks Completed", result["tasks_completed"])
                cols[2].metric("Words approx", len(result["final_content"].split()))
            
            with tab4:
                st.markdown(f"### Overall Grade: **{quality_results['grade']}**")
                st.progress(quality_results['overall_score'] / 100)
                st.metric("Quality Score", f"{quality_results['overall_score']}/100")
                
                st.markdown("#### Detailed Scores")
                c1, c2, c3 = st.columns(3)
                c1.metric("Readability", quality_results['scores']['readability'])
                c2.metric("Structure", quality_results['scores']['structure'])
                c3.metric("Engagement", quality_results['scores']['engagement'])
                
                st.markdown("#### Recommendations")
                for rec in quality_results['recommendations']:
                    st.info(rec)
            
            with tab5:
                st.markdown("### Version History")
                history = vc.get_history(topic)
                st.table(history)
                
            # Download
            st.download_button(
                label="📥 Download Markdown",
                data=result["final_content"],
                file_name=f"content_{datetime.now().strftime('%Y%m%d')}.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.exception(e)

st.markdown("---")
st.caption("Built with CrewAI, DeepSeek, and ❤️ by Antigravity")
